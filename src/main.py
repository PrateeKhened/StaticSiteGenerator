import os
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from copystatic import copy_static
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    
    print("Deleting public directory...")
    print("Copying static files to public directory...")
    copy_static(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )

if __name__ == "__main__":
    main()