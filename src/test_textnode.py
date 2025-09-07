import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()