from django.shortcuts import render
from django.http import HttpResponse, Http404
import os
import markdown



def convert_md_to_html(md_content):
    """Convert Markdown content to HTML."""
    html_content = markdown.markdown(md_content)
    return html_content

def process_file(md_path, html_path):
    """Process a single Markdown file and write the HTML output."""
    with open(md_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    html_content = convert_md_to_html(md_content)

    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

def process_directory(input_dir, output_dir):
    """Process all Markdown files in a directory recursively."""
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                md_path = os.path.join(root, file)
                relative_path = os.path.relpath(md_path, input_dir)
                html_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.html')
                process_file(md_path, html_path)

def serve_docs(request, path='index.html'):
    docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs', 'output')
    file_path = os.path.join(docs_dir, path)
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return HttpResponse(file.read())
    else:
        raise Http404("File not found")
