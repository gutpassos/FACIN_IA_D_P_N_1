#!/usr/bin/env python3
"""
Script para converter FACIN_IA_ORGANIZATIONAL_MODEL.md para PDF
Utiliza markdown + weasyprint com CSS customizado
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path

# Caminhos dos arquivos
DOCS_DIR = Path(__file__).parent
MD_FILE = DOCS_DIR / "FACIN_IA_ORGANIZATIONAL_MODEL.md"
PDF_FILE = DOCS_DIR / "FACIN_IA_ORGANIZATIONAL_MODEL.pdf"

# CSS customizado para PDF bonito
CSS_STYLE = """
@page {
    size: A4;
    margin: 2.5cm 2cm;
    @top-center {
        content: "FACIN_IA - Modelo de Responsabilidade Organizacional";
        font-size: 9pt;
        color: #666;
        border-bottom: 1px solid #ddd;
        padding-bottom: 5px;
    }
    @bottom-center {
        content: "Página " counter(page) " de " counter(pages);
        font-size: 9pt;
        color: #666;
    }
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #333;
    max-width: 100%;
}

h1 {
    font-size: 24pt;
    color: #1a1a1a;
    border-bottom: 3px solid #0066cc;
    padding-bottom: 10px;
    margin-top: 30px;
    margin-bottom: 20px;
    page-break-after: avoid;
}

h2 {
    font-size: 18pt;
    color: #0066cc;
    margin-top: 25px;
    margin-bottom: 15px;
    page-break-after: avoid;
}

h3 {
    font-size: 14pt;
    color: #0088cc;
    margin-top: 20px;
    margin-bottom: 12px;
    page-break-after: avoid;
}

h4 {
    font-size: 12pt;
    color: #0099dd;
    margin-top: 15px;
    margin-bottom: 10px;
    page-break-after: avoid;
}

p {
    margin-bottom: 10px;
    text-align: justify;
}

ul, ol {
    margin-bottom: 15px;
    padding-left: 30px;
}

li {
    margin-bottom: 5px;
}

code {
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 3px;
    padding: 2px 6px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 9pt;
    color: #c7254e;
}

pre {
    background-color: #f8f8f8;
    border: 1px solid #ddd;
    border-left: 4px solid #0066cc;
    border-radius: 4px;
    padding: 12px;
    overflow-x: auto;
    margin-bottom: 20px;
    page-break-inside: avoid;
}

pre code {
    background-color: transparent;
    border: none;
    padding: 0;
    color: #333;
    font-size: 9pt;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
    font-size: 9pt;
    page-break-inside: avoid;
}

th {
    background-color: #0066cc;
    color: white;
    padding: 10px;
    text-align: left;
    font-weight: bold;
}

td {
    border: 1px solid #ddd;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

blockquote {
    border-left: 4px solid #0066cc;
    background-color: #f0f7ff;
    padding: 10px 15px;
    margin: 15px 0;
    font-style: italic;
}

a {
    color: #0066cc;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

hr {
    border: none;
    border-top: 2px solid #ddd;
    margin: 25px 0;
}

/* Estilos para emojis */
.emoji {
    font-size: 1.2em;
}

/* Evitar quebras ruins */
h1, h2, h3, h4, h5, h6 {
    page-break-after: avoid;
}

table, figure, pre {
    page-break-inside: avoid;
}

/* Estilo para caixas de código */
.codehilite {
    background-color: #f8f8f8;
    border-left: 4px solid #0066cc;
    padding: 12px;
}

/* Estilo para checkboxes */
input[type="checkbox"] {
    margin-right: 5px;
}

/* Primeira página - título */
.first-page {
    text-align: center;
    padding-top: 100px;
}

.first-page h1 {
    font-size: 32pt;
    margin-bottom: 30px;
}
"""

def convert_md_to_pdf():
    """Converte arquivo Markdown para PDF com estilização profissional"""
    
    print(f"📄 Lendo arquivo: {MD_FILE}")
    
    # Ler conteúdo do Markdown
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    print("🔄 Convertendo Markdown para HTML...")
    
    # Configurar extensões do Markdown
    md_extensions = [
        'markdown.extensions.extra',      # Tabelas, fenced code, etc.
        'markdown.extensions.codehilite', # Syntax highlighting
        'markdown.extensions.tables',     # Suporte a tabelas
        'markdown.extensions.toc',        # Table of contents
        'markdown.extensions.nl2br',      # Newline to <br>
        'markdown.extensions.sane_lists', # Listas melhores
    ]
    
    # Converter Markdown para HTML
    html_content = markdown.markdown(
        md_content,
        extensions=md_extensions,
        output_format='html5'
    )
    
    # Criar HTML completo com metadados
    full_html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="author" content="FACIN_IA Team">
        <meta name="description" content="Modelo de Responsabilidade Organizacional para FACIN_IA">
        <title>FACIN_IA - Modelo de Responsabilidade Organizacional</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    print("🎨 Aplicando estilização CSS...")
    
    # Converter HTML para PDF com WeasyPrint
    html_obj = HTML(string=full_html, base_url=str(DOCS_DIR))
    css_obj = CSS(string=CSS_STYLE)
    
    print(f"📊 Gerando PDF: {PDF_FILE}")
    
    html_obj.write_pdf(
        PDF_FILE,
        stylesheets=[css_obj],
        presentational_hints=True
    )
    
    print(f"✅ PDF gerado com sucesso: {PDF_FILE}")
    print(f"📦 Tamanho: {PDF_FILE.stat().st_size / 1024:.2f} KB")

if __name__ == "__main__":
    try:
        convert_md_to_pdf()
    except Exception as e:
        print(f"❌ Erro ao gerar PDF: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
