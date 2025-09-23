from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from copystatic import copy_static

def main():
    
    copy_static("static", "public")
    

if __name__ == "__main__":
    main()