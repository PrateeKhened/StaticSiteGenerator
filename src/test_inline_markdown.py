import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_italic_delimiter(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_multiple_delimiters(self):
        node = TextNode("This has **bold** and **more bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("more bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_delimiter_at_start(self):
        node = TextNode("**bold** at start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" at start", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_delimiter_at_end(self):
        node = TextNode("text ends with **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("text ends with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_entire_text_is_formatted(self):
        node = TextNode("**entirely bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("entirely bold", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_delimiter_found(self):
        node = TextNode("No formatting here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("No formatting here", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_nodes_input(self):
        nodes = [
            TextNode("First **bold** node", TextType.TEXT),
            TextNode("Second **bold** node", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("First ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" node", TextType.TEXT),
            TextNode("Second ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" node", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_non_text_nodes_passed_through(self):
        nodes = [
            TextNode("Regular text with **bold**", TextType.TEXT),
            TextNode("Already bold", TextType.BOLD),
            TextNode("More text with **bold**", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("Regular text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("Already bold", TextType.BOLD),
            TextNode("More text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected)

    def test_empty_string_sections_skipped(self):
        node = TextNode("**bold****another bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode("another bold", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected)

    def test_unclosed_delimiter_raises_error(self):
        node = TextNode("This has **unclosed bold", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertIn("invalid markdown, formatted section not closed", str(context.exception))

    def test_single_delimiter_raises_error(self):
        node = TextNode("Single **delimiter", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertIn("invalid markdown, formatted section not closed", str(context.exception))

    def test_empty_text_node(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = []
        self.assertEqual(new_nodes, expected)

    def test_whitespace_only_formatted_text(self):
        node = TextNode("Text with ** ** spaces", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode(" ", TextType.BOLD),
            TextNode(" spaces", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)


class TestExtractMarkdownImages(unittest.TestCase):

    def test_single_image(self):
        text = "This is text with an ![image](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = [("image", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_multiple_images(self):
        text = "Text with ![first image](https://example.com/first.png) and ![second image](https://example.com/second.jpg)"
        result = extract_markdown_images(text)
        expected = [
            ("first image", "https://example.com/first.png"),
            ("second image", "https://example.com/second.jpg")
        ]
        self.assertEqual(result, expected)

    def test_image_with_empty_alt_text(self):
        text = "Image with no alt text: ![](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = [("", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_image_with_empty_url(self):
        text = "Image with no URL: ![alt text]()"
        result = extract_markdown_images(text)
        expected = [("alt text", "")]
        self.assertEqual(result, expected)

    def test_image_with_spaces_in_alt_text(self):
        text = "![This is a long alt text with spaces](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = [("This is a long alt text with spaces", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_image_with_special_characters_in_alt_text(self):
        text = "![Alt with $pecial ch@r$ & symbols!](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = [("Alt with $pecial ch@r$ & symbols!", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_image_with_relative_path(self):
        text = "Local image: ![local](./images/local.png)"
        result = extract_markdown_images(text)
        expected = [("local", "./images/local.png")]
        self.assertEqual(result, expected)

    def test_no_images_in_text(self):
        text = "This text has no images, just regular text and [regular links](https://example.com)"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_malformed_image_missing_exclamation(self):
        text = "This is not an image: [alt text](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_malformed_image_missing_brackets(self):
        text = "Malformed: !alt text](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_malformed_image_missing_parentheses(self):
        text = "Malformed: ![alt text]https://example.com/image.png"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_image_with_nested_brackets_in_alt_not_matched(self):
        text = "![Image with [nested] brackets](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_image_with_nested_parentheses_in_url_not_matched(self):
        text = "![alt](https://example.com/path(with)parentheses.png)"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_empty_string(self):
        text = ""
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_multiple_images_with_text_between(self):
        text = "Start ![first](url1.png) middle text ![second](url2.jpg) end text ![third](url3.gif)"
        result = extract_markdown_images(text)
        expected = [
            ("first", "url1.png"),
            ("second", "url2.jpg"),
            ("third", "url3.gif")
        ]
        self.assertEqual(result, expected)

    def test_image_with_underscores_and_hyphens(self):
        text = "![file_name-test](path/to/image_file-name.png)"
        result = extract_markdown_images(text)
        expected = [("file_name-test", "path/to/image_file-name.png")]
        self.assertEqual(result, expected)

    def test_image_with_numbers(self):
        text = "![image123](file123.png)"
        result = extract_markdown_images(text)
        expected = [("image123", "file123.png")]
        self.assertEqual(result, expected)

    def test_consecutive_images(self):
        text = "![first](img1.png)![second](img2.png)"
        result = extract_markdown_images(text)
        expected = [
            ("first", "img1.png"),
            ("second", "img2.png")
        ]
        self.assertEqual(result, expected)


class TestExtractMarkdownLinks(unittest.TestCase):

    def test_single_link(self):
        text = "This is text with a [link](https://example.com)"
        result = extract_markdown_links(text)
        expected = [("link", "https://example.com")]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        text = "Text with [first link](https://example.com) and [second link](https://google.com)"
        result = extract_markdown_links(text)
        expected = [
            ("first link", "https://example.com"),
            ("second link", "https://google.com")
        ]
        self.assertEqual(result, expected)

    def test_link_with_empty_text(self):
        text = "Link with no text: [](https://example.com)"
        result = extract_markdown_links(text)
        expected = [("", "https://example.com")]
        self.assertEqual(result, expected)

    def test_link_with_empty_url(self):
        text = "Link with no URL: [link text]()"
        result = extract_markdown_links(text)
        expected = [("link text", "")]
        self.assertEqual(result, expected)

    def test_link_with_spaces_in_text(self):
        text = "[This is a long link text with spaces](https://example.com)"
        result = extract_markdown_links(text)
        expected = [("This is a long link text with spaces", "https://example.com")]
        self.assertEqual(result, expected)

    def test_link_with_special_characters_in_text(self):
        text = "[Link with $pecial ch@r$ & symbols!](https://example.com)"
        result = extract_markdown_links(text)
        expected = [("Link with $pecial ch@r$ & symbols!", "https://example.com")]
        self.assertEqual(result, expected)

    def test_link_with_relative_path(self):
        text = "Local link: [local page](./pages/about.html)"
        result = extract_markdown_links(text)
        expected = [("local page", "./pages/about.html")]
        self.assertEqual(result, expected)

    def test_link_with_anchor(self):
        text = "Link with anchor: [section](https://example.com/page#section)"
        result = extract_markdown_links(text)
        expected = [("section", "https://example.com/page#section")]
        self.assertEqual(result, expected)

    def test_link_with_query_parameters(self):
        text = "Link with params: [search](https://example.com/search?q=test&type=all)"
        result = extract_markdown_links(text)
        expected = [("search", "https://example.com/search?q=test&type=all")]
        self.assertEqual(result, expected)

    def test_no_links_in_text(self):
        text = "This text has no links, just regular text and ![images](https://example.com/image.png)"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_malformed_link_missing_brackets(self):
        text = "Malformed: link text](https://example.com)"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_malformed_link_missing_parentheses(self):
        text = "Malformed: [link text]https://example.com"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_link_with_nested_brackets_in_text_not_matched(self):
        text = "[Link with [nested] brackets](https://example.com)"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_link_with_nested_parentheses_in_url_not_matched(self):
        text = "[link](https://example.com/path(with)parentheses)"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_empty_string(self):
        text = ""
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_multiple_links_with_text_between(self):
        text = "Start [first](url1.com) middle text [second](url2.com) end text [third](url3.com)"
        result = extract_markdown_links(text)
        expected = [
            ("first", "url1.com"),
            ("second", "url2.com"),
            ("third", "url3.com")
        ]
        self.assertEqual(result, expected)

    def test_links_and_images_mixed(self):
        text = "Mixed content: [link](https://example.com) and ![image](image.png) and [another link](test.com)"
        result = extract_markdown_links(text)
        expected = [
            ("link", "https://example.com"),
            ("another link", "test.com")
        ]
        self.assertEqual(result, expected)

    def test_link_with_markdown_in_text(self):
        text = "[Link with **bold** text](https://example.com)"
        result = extract_markdown_links(text)
        expected = [("Link with **bold** text", "https://example.com")]
        self.assertEqual(result, expected)

    def test_consecutive_links(self):
        text = "[first](url1.com)[second](url2.com)"
        result = extract_markdown_links(text)
        expected = [
            ("first", "url1.com"),
            ("second", "url2.com")
        ]
        self.assertEqual(result, expected)

    def test_image_link_not_matched_by_link_extractor(self):
        text = "This ![image](image.png) should not be matched as a link"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_link_with_underscores_and_hyphens(self):
        text = "[link_name-test](path/to/page_name-file.html)"
        result = extract_markdown_links(text)
        expected = [("link_name-test", "path/to/page_name-file.html")]
        self.assertEqual(result, expected)

    def test_link_with_numbers(self):
        text = "[link123](page123.html)"
        result = extract_markdown_links(text)
        expected = [("link123", "page123.html")]
        self.assertEqual(result, expected)

    def test_link_immediately_after_image(self):
        text = "![image](img.png)[link](page.html)"
        result = extract_markdown_links(text)
        expected = [("link", "page.html")]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()