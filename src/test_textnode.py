import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a code", TextType.CODE)
        self.assertNotEqual(node, node2)
    
    def test_eq_image(self):
        node = TextNode("This is a image", TextType.IMAGE, "public/image.png")
        node2 = TextNode("This is a image", TextType.IMAGE, "public/image.png")
        self.assertEqual(node, node2)
    
    def test_not_eq_texttype(self):
        node = TextNode("This is a code", TextType.CODE)
        node2 = TextNode("This is a code", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_image(self):
        node = TextNode("This is a image", TextType.IMAGE, "public/image1.png")
        node2 = TextNode("This is a image", TextType.IMAGE, "public/image2.png")
        self.assertNotEqual(node, node2)

class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
        node = TextNode("print('hello world')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hello world')")

    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        node = TextNode("Alt text for image", TextType.IMAGE, "public/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "public/image.png", "alt": "Alt text for image"})

    def test_invalid_text_type(self):
        node = TextNode("Invalid type", "invalid")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()