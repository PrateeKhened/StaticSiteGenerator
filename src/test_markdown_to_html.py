import unittest
from markdown_to_html import markdown_to_html_node, extract_title
from htmlnode import ParentNode, LeafNode


class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_simple_paragraph(self):
        markdown = "This is a simple paragraph."
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("p", [LeafNode(None, "This is a simple paragraph.")])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_multiple_paragraphs(self):
        markdown = """First paragraph here.

Second paragraph here."""
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("p", [LeafNode(None, "First paragraph here.")]),
            ParentNode("p", [LeafNode(None, "Second paragraph here.")])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_heading_h1(self):
        markdown = "# Main Heading"
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("h1", [LeafNode(None, "Main Heading")])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_heading_h2(self):
        markdown = "## Sub Heading"
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("h2", [LeafNode(None, "Sub Heading")])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_heading_h6(self):
        markdown = "###### Small Heading"
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("h6", [LeafNode(None, "Small Heading")])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_code_block(self):
        markdown = """```
print("Hello World")
x = 5
```"""
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("pre", [
                LeafNode("code", 'print("Hello World")\nx = 5\n')
            ])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_code_block_with_language(self):
        markdown = """```python
def hello():
    print("Hello")
```"""
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("pre", [
                LeafNode("code", 'def hello():\nprint("Hello")\n')
            ])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_unordered_list_simple(self):
        markdown = """- First item
- Second item
- Third item"""
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("ul", [
                ParentNode("li", [LeafNode(None, "First item")]),
                ParentNode("li", [LeafNode(None, "Second item")]),
                ParentNode("li", [LeafNode(None, "Third item")])
            ])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_ordered_list_simple(self):
        markdown = """1. First item
2. Second item
3. Third item"""
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("ol", [
                ParentNode("li", [LeafNode(None, "First item")]),
                ParentNode("li", [LeafNode(None, "Second item")]),
                ParentNode("li", [LeafNode(None, "Third item")])
            ])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_quote_single_line(self):
        markdown = "> This is a quote"
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("blockquote", [LeafNode(None, "This is a quote")])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_quote_multiline(self):
        markdown = """> This is a quote
> spanning multiple lines
> with more content"""
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            ParentNode("blockquote", [
                LeafNode(None, "This is a quote\nspanning multiple lines\nwith more content")
            ])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_mixed_content(self):
        markdown = """# Main Title

This is a paragraph with text.

## Subtitle

Another paragraph here.

- List item 1
- List item 2

> A quote block

```
some code
```"""
        result = markdown_to_html_node(markdown)

        # Verify it's a div with the correct number of children
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 7)

        # Check the types of each child
        self.assertEqual(result.children[0].tag, "h1")
        self.assertEqual(result.children[1].tag, "p")
        self.assertEqual(result.children[2].tag, "h2")
        self.assertEqual(result.children[3].tag, "p")
        self.assertEqual(result.children[4].tag, "ul")
        self.assertEqual(result.children[5].tag, "blockquote")
        self.assertEqual(result.children[6].tag, "pre")

    def test_paragraph_with_inline_formatting(self):
        markdown = "This has **bold** and *italic* text."
        result = markdown_to_html_node(markdown)

        # Should create a paragraph with multiple child nodes for formatting
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 1)
        self.assertEqual(result.children[0].tag, "p")

        # The paragraph should have multiple children for the inline formatting
        paragraph = result.children[0]
        self.assertTrue(len(paragraph.children) > 1)

    def test_empty_markdown(self):
        markdown = ""
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_whitespace_only_markdown(self):
        markdown = "   \n\n   \n\n   "
        result = markdown_to_html_node(markdown)

        expected = ParentNode("div", [])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_heading_without_text(self):
        markdown = "#"
        result = markdown_to_html_node(markdown)

        # "#" without space is treated as paragraph, not heading
        expected = ParentNode("div", [
            ParentNode("p", [LeafNode(None, "#")])
        ])

        self.assertEqual(result.to_html(), expected.to_html())

    def test_list_with_inline_formatting(self):
        markdown = """- Item with **bold** text
- Item with *italic* text"""
        result = markdown_to_html_node(markdown)

        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 1)
        self.assertEqual(result.children[0].tag, "ul")

        # Each list item should have formatting
        ul = result.children[0]
        self.assertEqual(len(ul.children), 2)
        self.assertEqual(ul.children[0].tag, "li")
        self.assertEqual(ul.children[1].tag, "li")

    def test_quote_with_inline_formatting(self):
        markdown = "> This quote has **bold** text"
        result = markdown_to_html_node(markdown)

        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 1)
        self.assertEqual(result.children[0].tag, "blockquote")

        # The blockquote should have multiple children for formatting
        blockquote = result.children[0]
        self.assertTrue(len(blockquote.children) > 1)

    def test_consecutive_code_blocks(self):
        markdown = """```
first code block
```

```
second code block
```"""
        result = markdown_to_html_node(markdown)

        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 2)
        self.assertEqual(result.children[0].tag, "pre")
        self.assertEqual(result.children[1].tag, "pre")

    def test_nested_list_items_not_supported(self):
        # The current implementation doesn't handle nested lists
        markdown = """- Top level item
  - Nested item
- Another top level"""
        result = markdown_to_html_node(markdown)

        # Should still create a valid structure even if nesting isn't handled
        self.assertEqual(result.tag, "div")
        self.assertTrue(len(result.children) >= 1)


class TestExtractTitle(unittest.TestCase):

    def test_extract_title_simple(self):
        markdown = "# Hello"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello")

    def test_extract_title_with_whitespace(self):
        markdown = "#   Hello World   "
        result = extract_title(markdown)
        self.assertEqual(result, "Hello World")

    def test_extract_title_with_content_after(self):
        markdown = """# Main Title

This is some content after the title.

## Subtitle

More content here."""
        result = extract_title(markdown)
        self.assertEqual(result, "Main Title")

    def test_extract_title_with_inline_formatting(self):
        markdown = "# Title with **bold** and *italic* text"
        result = extract_title(markdown)
        self.assertEqual(result, "Title with **bold** and *italic* text")

    def test_extract_title_ignores_h2(self):
        markdown = """## Not the title

# The Real Title

More content."""
        result = extract_title(markdown)
        self.assertEqual(result, "The Real Title")

    def test_extract_title_ignores_h3_through_h6(self):
        markdown = """### Level 3
#### Level 4
##### Level 5
###### Level 6

# Level 1 Title

More content."""
        result = extract_title(markdown)
        self.assertEqual(result, "Level 1 Title")

    def test_extract_title_no_h1_header_raises_exception(self):
        markdown = """## This is h2

### This is h3

This is just text."""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No h1 header found")

    def test_extract_title_empty_markdown_raises_exception(self):
        markdown = ""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No h1 header found")

    def test_extract_title_only_whitespace_raises_exception(self):
        markdown = "   \n\n   \n   "
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No h1 header found")

    def test_extract_title_invalid_h1_format_raises_exception(self):
        markdown = """#No space after hash

This is not a valid h1 header."""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No h1 header found")

    def test_extract_title_multiple_h1_returns_first(self):
        markdown = """# First Title

Some content.

# Second Title

More content."""
        result = extract_title(markdown)
        self.assertEqual(result, "First Title")

    def test_extract_title_h1_with_special_characters(self):
        markdown = "# Title with $pecial Ch@racters & Symbols!"
        result = extract_title(markdown)
        self.assertEqual(result, "Title with $pecial Ch@racters & Symbols!")

    def test_extract_title_h1_with_numbers(self):
        markdown = "# 123 Numbered Title 456"
        result = extract_title(markdown)
        self.assertEqual(result, "123 Numbered Title 456")

    def test_extract_title_single_word(self):
        markdown = "# Title"
        result = extract_title(markdown)
        self.assertEqual(result, "Title")


if __name__ == "__main__":
    unittest.main()