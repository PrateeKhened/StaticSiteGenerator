import os
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from copystatic import copy_static
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    
    print("Deleting public directory...")
    print("Copying static files to public directory...")
    copy_static(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
    )

if __name__ == "__main__":
    main()