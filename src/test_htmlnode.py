import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertNotEqual(parent_node.to_html(), "<div> <span>child</span> </div>")

    def test_parent_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "First paragraph")
        child2 = LeafNode("p", "Second paragraph")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><p>First paragraph</p><p>Second paragraph</p></div>")

    def test_parent_to_html_with_props(self):
        child_node = LeafNode("span", "content")
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        self.assertEqual(parent_node.to_html(), '<div class="container" id="main"><span>content</span></div>')

    def test_parent_to_html_nested_parents(self):
        inner_child = LeafNode("em", "emphasized")
        inner_parent = ParentNode("p", [inner_child])
        outer_parent = ParentNode("article", [inner_parent])
        self.assertEqual(outer_parent.to_html(), "<article><p><em>emphasized</em></p></article>")

    def test_parent_to_html_mixed_children(self):
        leaf_child = LeafNode("span", "leaf text")
        nested_leaf = LeafNode("strong", "bold text")
        parent_child = ParentNode("p", [nested_leaf])
        main_parent = ParentNode("div", [leaf_child, parent_child])
        self.assertEqual(main_parent.to_html(), "<div><span>leaf text</span><p><strong>bold text</strong></p></div>")

    def test_parent_to_html_no_tag_raises_error(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_parent_to_html_no_children_raises_error(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_parent_to_html_empty_children_list(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_parent_to_html_complex_nesting(self):
        deep_child = LeafNode("code", "print('hello')")
        level3 = ParentNode("pre", [deep_child])
        level2 = ParentNode("div", [level3], {"class": "code-block"})
        level1 = ParentNode("section", [level2])
        expected = '<section><div class="code-block"><pre><code>print(\'hello\')</code></pre></div></section>'
        self.assertEqual(level1.to_html(), expected)

    def test_parent_to_html_not_equal_wrong_tag(self):
        child_node = LeafNode("span", "content")
        parent_node = ParentNode("div", [child_node])
        self.assertNotEqual(parent_node.to_html(), "<section><span>content</span></section>")

    def test_parent_to_html_not_equal_wrong_child_content(self):
        child_node = LeafNode("p", "original text")
        parent_node = ParentNode("div", [child_node])
        self.assertNotEqual(parent_node.to_html(), "<div><p>different text</p></div>")


if __name__ == "__main__":
    unittest.main()