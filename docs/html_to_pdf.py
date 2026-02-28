#!/usr/bin/env python3
"""
Script para converter HTML para PDF usando Playwright
Converte FACIN_IA_ORGANIZATIONAL_MODEL.html para PDF
"""

from playwright.sync_api import sync_playwright
from pathlib import Path
import sys

# Caminhos dos arquivos
DOCS_DIR = Path(__file__).parent
HTML_FILE = DOCS_DIR / "FACIN_IA_ORGANIZATIONAL_MODEL.html"
PDF_FILE = DOCS_DIR / "FACIN_IA_ORGANIZATIONAL_MODEL.pdf"

def html_to_pdf():
    """Converte HTML para PDF usando Playwright/Chromium"""
    
    print(f"📄 Arquivo HTML: {HTML_FILE}")
    
    if not HTML_FILE.exists():
        print(f"❌ Erro: Arquivo HTML não encontrado: {HTML_FILE}")
        return False
    
    print("🌐 Iniciando navegador Chromium...")
    
    with sync_playwright() as p:
        # Lançar navegador headless
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print(f"📖 Carregando HTML...")
        
        # Carregar arquivo HTML
        page.goto(f"file:///{HTML_FILE.absolute().as_posix()}")
        
        # Aguardar carregamento completo
        page.wait_for_load_state("networkidle")
        
        print("📊 Gerando PDF...")
        
        # Configurações de PDF profissionais
        page.pdf(
            path=str(PDF_FILE),
            format="A4",
            margin={
                "top": "2cm",
                "right": "2cm",
                "bottom": "2cm",
                "left": "2cm"
            },
            print_background=True,
            display_header_footer=True,
            header_template="""
                <div style="font-size: 9px; text-align: center; width: 100%; 
                            color: #666; border-bottom: 1px solid #ddd; 
                            padding-bottom: 5px; margin: 0 2cm;">
                    FACIN_IA - Modelo de Responsabilidade Organizacional
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
    
    if PDF_FILE.exists():
        file_size = PDF_FILE.stat().st_size
        print(f"✅ PDF gerado com sucesso!")
        print(f"📁 Local: {PDF_FILE}")
        print(f"📦 Tamanho: {file_size / 1024:.2f} KB ({file_size / (1024*1024):.2f} MB)")
        return True
    else:
        print("❌ Erro: PDF não foi gerado")
        return False

if __name__ == "__main__":
    try:
        success = html_to_pdf()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Erro ao gerar PDF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
