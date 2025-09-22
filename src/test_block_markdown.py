import unittest
from block_markdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
        blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_empty_markdown(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_block(self):
        md = "This is a single block of text"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single block of text"])

    def test_blocks_with_only_whitespace(self):
        md = "   \n\n   \n\n   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_blocks_with_leading_trailing_whitespace(self):
        md = "   This block has leading whitespace   \n\n   Another block with whitespace   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This block has leading whitespace",
                "Another block with whitespace"
            ]
        )

    def test_blocks_with_mixed_line_endings(self):
        md = "First block\nwith multiple lines\n\nSecond block\nwith more lines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First block\nwith multiple lines",
                "Second block\nwith more lines"
            ]
        )

    def test_blocks_with_code_formatting(self):
        md = """```python
                    def hello():
                        print("Hello")
                    ```

                    This is a regular paragraph

                    ```javascript
                    console.log("Hello");
            ```"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                '```python\ndef hello():\nprint("Hello")\n```',
                "This is a regular paragraph",
                '```javascript\nconsole.log("Hello");\n```'
            ]
        )

    def test_blocks_with_headers(self):
        md = """# Main Header

## Subheader

### Another header
With some content below

Regular paragraph"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Main Header",
                "## Subheader",
                "### Another header\nWith some content below",
                "Regular paragraph"
            ]
        )

    def test_blocks_with_quotes(self):
        md = """> This is a quote
> spanning multiple lines

Normal paragraph

> Another quote"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "> This is a quote\n> spanning multiple lines",
                "Normal paragraph",
                "> Another quote"
            ]
        )

    def test_blocks_with_lists(self):
        md = """1. First item
2. Second item
3. Third item

- Unordered item 1
- Unordered item 2

* Another unordered list
* With asterisks"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "1. First item\n2. Second item\n3. Third item",
                "- Unordered item 1\n- Unordered item 2",
                "* Another unordered list\n* With asterisks"
            ]
        )

    def test_blocks_with_many_empty_lines(self):
        md = """First block



Second block




Third block"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First block",
                "Second block",
                "Third block"
            ]
        )

    def test_blocks_with_tabs_and_spaces(self):
        md = "\tBlock with tab at start\n\n    Block with spaces    \n\n\t\tAnother tab block\t\t"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Block with tab at start",
                "Block with spaces",
                "Another tab block"
            ]
        )


if __name__ == "__main__":
    unittest.main()