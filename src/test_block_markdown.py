import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

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


class TestBlockToBlockType(unittest.TestCase):

    def test_paragraph_block(self):
        block = "This is a regular paragraph with some text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_multiline(self):
        block = "This is a paragraph\nwith multiple lines\nof text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_h1(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_h2(self):
        block = "## This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_h3(self):
        block = "### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_h4(self):
        block = "#### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_h5(self):
        block = "##### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_h6(self):
        block = "###### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_with_content(self):
        block = "# Main Title\nWith some content below"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_not_heading_no_space(self):
        block = "#This is not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_not_heading_seven_hashes(self):
        block = "####### This is not a valid heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block_simple(self):
        block = "```\ncode here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_with_language(self):
        block = "```python\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_multiline(self):
        block = "```\nline 1\nline 2\nline 3\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_not_code_block_single_line(self):
        block = "```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_not_code_block_no_closing(self):
        block = "```\ncode here"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_single_line(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_multiline(self):
        block = "> This is a quote\n> spanning multiple lines\n> with more content"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_with_spaces(self):
        block = "> Quote line 1\n> Quote line 2"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_not_quote_mixed_lines(self):
        block = "> This starts as a quote\nBut this line is not quoted"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_not_quote_no_space(self):
        block = ">Not a quote without space"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_single_item(self):
        block = "- List item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_multiple_items(self):
        block = "- First item\n- Second item\n- Third item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_with_content(self):
        block = "- Item with longer content\n- Another item here"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_not_unordered_list_mixed_lines(self):
        block = "- This starts as a list\nBut this is not a list item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_not_unordered_list_no_space(self):
        block = "-Not a list without space"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_single_item(self):
        block = "1. First item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_multiple_items(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_longer_sequence(self):
        block = "1. Item one\n2. Item two\n3. Item three\n4. Item four\n5. Item five"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_not_ordered_list_wrong_numbering(self):
        block = "1. First item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_not_ordered_list_not_starting_with_one(self):
        block = "2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_not_ordered_list_mixed_lines(self):
        block = "1. This starts as a list\nBut this is not numbered"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_not_ordered_list_no_space(self):
        block = "1.Not a list without space"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_empty_block(self):
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_whitespace_only_block(self):
        block = "   \n   \n   "
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_edge_case_hash_in_middle(self):
        block = "This has # hash in middle"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_edge_case_dash_in_middle(self):
        block = "This has - dash in middle"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_edge_case_greater_than_in_middle(self):
        block = "This has > symbol in middle"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()