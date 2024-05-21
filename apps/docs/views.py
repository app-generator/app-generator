from django.shortcuts import render
from django.http import Http404
import os
import markdown
import json
from collections import defaultdict

def process_file(md_path, html_path):
    """Process a single Markdown file and write the HTML output."""
    with open(md_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    html_content = convert_md_to_html(md_content)

    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)


def convert_md_to_html(md_content):
    """Convert Markdown content to HTML."""
    html_content = markdown.markdown(md_content)
    return html_content


def build_file_tree(directory, base_dir):
    """Build a nested dictionary representing the file structure."""
    file_tree = defaultdict(dict)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_path = os.path.join(root, file)
                relative_path = os.path.relpath(md_path, base_dir)
                html_path = os.path.splitext(relative_path)[0] + '.html'
                parts = relative_path.split(os.sep)
                d = file_tree
                for part in parts[:-1]:
                    d = d.setdefault(part, {})
                d[parts[-1]] = html_path
    return file_tree


def process_directory(input_dir, output_dir):
    """Process all Markdown files in a directory recursively and generate a nested structure of HTML files."""
    file_tree = build_file_tree(input_dir, input_dir)
    
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                md_path = os.path.join(root, file)
                relative_path = os.path.relpath(md_path, input_dir)
                html_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.html')
                process_file(md_path, html_path)
    
    # Save the file tree to a JSON file
    pages_json_path = os.path.join(output_dir, 'pages.json')
    with open(pages_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(file_tree, json_file, indent=2)





def serve_docs(request, path='index.html'):
    docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs', 'output')
    file_path = os.path.join(docs_dir, path)
    
    # Load the nested file structure from the JSON file
    pages_json_path = os.path.join(docs_dir, 'pages.json')
    with open(pages_json_path, 'r', encoding='utf-8') as json_file:
        pages = json.load(json_file)
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Render the HTML content as a Django template
        context = {
            'content': html_content,
            'pages': pages
        }

        return render(request, 'layouts/base-docs.html', context)
    else:
        raise Http404("File not found")
