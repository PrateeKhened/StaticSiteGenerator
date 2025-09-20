import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_eq(self):
        node = HTMLNode("a", props={"href": "https://www.google.com","target": "_blank",})
        res = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), res)
    
    def test_props_to_html_with_no_props(self):
        node = HTMLNode("p", "india is my country")
        res = ' href="india is my country"'
        self.assertNotEqual(node.props_to_html(), res)
    
    def test_props_to_html_not_eq(self):
        node = HTMLNode("img", props={"src": "/logo.png", "alt": "Logo"})
        res = ' src="/logo1.png" alt="Logo1"'
        self.assertNotEqual(node.props_to_html(), res)
    
    def test_props_to_html_no_props_eq(self):
        node = HTMLNode("p", "india is my country")
        res = ''
        self.assertEqual(node.props_to_html(), res)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), '<p>Hello, world!</p>')
    
    def test_leaf_to_html_props_eq(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        res = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), res)
    
    def test_leaf_to_html_not_eq(self):
        node = LeafNode("p", "india is my country and all indians are my brothers and sisters")
        self.assertNotEqual(node.to_html(), '<p>USA is my country and all Americans are my brothers and sisters</p>')
    
    def test_leaf_to_html_not_eq(self):
        node = LeafNode("p", "india is my country and all indians are my brothers and sisters")
        self.assertNotEqual(node.to_html(), '<h1>india is my country and all indians are my brothers and sisters</h1>')


if __name__ == "__main__":
    unittest.main()