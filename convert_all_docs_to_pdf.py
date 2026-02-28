#!/usr/bin/env python3
"""
Script para converter todos os arquivos Markdown para PDF
Processa arquivos nas pastas docs/ e errors/
Usa Pandoc (MD->HTML) + Playwright (HTML->PDF)
"""

from playwright.sync_api import sync_playwright
from pathlib import Path
import subprocess
import sys
import time

# Diretório raiz do projeto
ROOT_DIR = Path(__file__).parent
DOCS_DIR = ROOT_DIR / "docs"
ERRORS_DIR = ROOT_DIR / "errors"

def find_markdown_files():
    """Encontra todos os arquivos .md nas pastas docs/ e errors/"""
    md_files = []
    
    # Buscar em docs/ (recursivo)
    if DOCS_DIR.exists():
        md_files.extend(DOCS_DIR.rglob("*.md"))
    
    # Buscar em errors/
    if ERRORS_DIR.exists():
        md_files.extend(ERRORS_DIR.glob("*.md"))
    
    return sorted(md_files)

def convert_md_to_html(md_file: Path) -> Path:
    """Converte Markdown para HTML usando Pandoc"""
    html_file = md_file.with_suffix(".html")
    
    # Extrair título do arquivo
    title = md_file.stem.replace("_", " ").title()
    
    # Comando Pandoc
    cmd = [
        "pandoc",
        str(md_file),
        "-o", str(html_file),
        "--standalone",
        "--toc",
        "--toc-depth=3",
        "--number-sections",
        "--metadata", f"title={title}",
        "--css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css",
        "-V", "lang=pt-BR"
    ]
    
    print(f"  🔄 MD → HTML: {md_file.name}")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return html_file
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Erro Pandoc: {e.stderr}")
        return None

def convert_html_to_pdf(html_file: Path) -> Path:
    """Converte HTML para PDF usando Playwright"""
    pdf_file = html_file.with_suffix(".pdf")
    
    if not html_file.exists():
        print(f"  ❌ HTML não encontrado: {html_file}")
        return None
    
    print(f"  📊 HTML → PDF: {html_file.name}")
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Carregar HTML
            page.goto(f"file:///{html_file.absolute().as_posix()}")
            page.wait_for_load_state("networkidle")
            
            # Gerar PDF
            page.pdf(
                path=str(pdf_file),
                format="A4",
                margin={
                    "top": "2cm",
                    "right": "2cm",
                    "bottom": "2cm",
                    "left": "2cm"
                },
                print_background=True,
                display_header_footer=True,
                header_template=f"""
                    <div style="font-size: 9px; text-align: center; width: 100%; 
                                color: #666; border-bottom: 1px solid #ddd; 
                                padding-bottom: 5px; margin: 0 2cm;">
                        {html_file.stem.replace('_', ' ').title()}
                    </div>
                """,
                footer_template="""
                    <div style="font-size: 9px; text-align: center; width: 100%; 
                                color: #666; margin: 0 2cm;">
                        Página <span class="pageNumber"></span> de <span class="totalPages"></span>
                    </div>
                """,
                prefer_css_page_size=False,
                scale=0.95
            )
            
            browser.close()
        
        return pdf_file
    except Exception as e:
        print(f"  ❌ Erro Playwright: {e}")
        return None

def cleanup_html(html_file: Path):
    """Remove arquivo HTML intermediário"""
    if html_file and html_file.exists():
        html_file.unlink()

def main():
    """Processa todos os arquivos Markdown"""
    print("=" * 70)
    print("📚 Conversor em Lote: Markdown → PDF")
    print("=" * 70)
    print()
    
    # Encontrar arquivos
    md_files = find_markdown_files()
    
    if not md_files:
        print("⚠️  Nenhum arquivo .md encontrado")
        return
    
    print(f"📋 Encontrados {len(md_files)} arquivo(s) Markdown:\n")
    
    for md_file in md_files:
        rel_path = md_file.relative_to(ROOT_DIR)
        print(f"  • {rel_path}")
    
    print()
    print("=" * 70)
    print()
    
    # Estatísticas
    stats = {
        "total": len(md_files),
        "success": 0,
        "failed": 0,
        "skipped": 0
    }
    
    # Processar cada arquivo
    for idx, md_file in enumerate(md_files, 1):
        rel_path = md_file.relative_to(ROOT_DIR)
        print(f"[{idx}/{stats['total']}] 📄 {rel_path}")
        
        # Verificar se PDF já existe
        pdf_file = md_file.with_suffix(".pdf")
        
        # Converter MD → HTML
        html_file = convert_md_to_html(md_file)
        
        if html_file:
            # Converter HTML → PDF
            result_pdf = convert_html_to_pdf(html_file)
            
            # Limpar HTML intermediário
            cleanup_html(html_file)
            
            if result_pdf and result_pdf.exists():
                file_size = result_pdf.stat().st_size
                print(f"  ✅ Sucesso! ({file_size / 1024:.1f} KB)")
                stats["success"] += 1
            else:
                print(f"  ❌ Falhou")
                stats["failed"] += 1
        else:
            print(f"  ❌ Falhou na conversão HTML")
            stats["failed"] += 1
        
        print()
    
    # Resumo final
    print("=" * 70)
    print("📊 RESUMO DA CONVERSÃO")
    print("=" * 70)
    print(f"✅ Sucesso:  {stats['success']}/{stats['total']}")
    print(f"❌ Falhas:   {stats['failed']}/{stats['total']}")
    
    if stats['success'] > 0:
        print()
        print("📁 Arquivos PDF gerados:")
        for md_file in md_files:
            pdf_file = md_file.with_suffix(".pdf")
            if pdf_file.exists():
                rel_path = pdf_file.relative_to(ROOT_DIR)
                size_kb = pdf_file.stat().st_size / 1024
                print(f"  • {rel_path} ({size_kb:.1f} KB)")
    
    print()
    print("✅ Conversão concluída!" if stats['failed'] == 0 else "⚠️  Conversão concluída com erros")
    
    return 0 if stats['failed'] == 0 else 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n⚠️  Conversão interrompida pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro fatal: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
