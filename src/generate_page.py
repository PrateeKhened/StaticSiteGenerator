from pathlib import Path
import os
from markdown_to_html import markdown_to_html_node, extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(from_path):
            if file.endswith(".md"):
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.exists(from_path):
        raise FileNotFoundError(f"Markdown file not found: {from_path}")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")

    _, ext = os.path.splitext(from_path)
    if ext.lower() != ".md":
        raise ValueError(f"Expected a .md file, got: {ext}")
    with open(from_path, "r") as f:
        markdown_text = f.read()

    _, ext = os.path.splitext(template_path)
    if ext.lower() != ".html":
        raise ValueError(f"Expected a .html file, got: {ext}")
    with open(template_path, "r") as f:
        template_text = f.read()
    
    html = markdown_to_html_node(markdown_text).to_html()
    title = extract_title(markdown_text)

    output = template_text.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(output)