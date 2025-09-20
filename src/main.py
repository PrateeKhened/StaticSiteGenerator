from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textnode)
    htmlnode = HTMLNode("p", "india is a country", props={"href": "beautifulindia.com"})
    print(htmlnode)
    leafnode = LeafNode("p", "india is a country", props={"href": "beautifulindia.com"})
    print(leafnode)
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parentnode = ParentNode("div", [child_node])
    print(parentnode)


main()