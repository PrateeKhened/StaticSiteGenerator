import unittest
from htmlnode import HTMLNode

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
    

if __name__ == "__main__":
    unittest.main()