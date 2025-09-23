# Static Site Generator

A Python-based static site generator that converts markdown files to static websites with a clean, modular architecture.

## 🚀 Features

- **Complete Markdown Processing** - Full markdown-to-HTML conversion pipeline
- **Block-Level Elements** - Support for headings, paragraphs, code blocks, quotes, and lists
- **Quote Block Enhancement** - Proper handling of quotes with empty lines (fixed recent issue)
- **Title Extraction** - Extract h1 headers from markdown for page titles
- **Inline Formatting** - Bold, italic, code, links, and images with delimiter processing
- **Text Processing Pipeline** - Clean separation between text representation and HTML generation
- **Modular Architecture** - Well-structured codebase with clear separation of concerns
- **Comprehensive Testing** - Extensive test suite with 130+ test cases covering all components

## 📁 Project Structure

```
StaticSiteGenerator/
├── src/
│   ├── htmlnode.py              # HTML generation layer
│   ├── textnode.py              # Text representation layer
│   ├── inline_markdown.py       # Inline markdown processing utilities
│   ├── block_markdown.py        # Block-level markdown processing
│   ├── markdown_to_html.py      # Complete markdown-to-HTML conversion
│   ├── main.py                 # Application entry point
│   ├── test_htmlnode.py        # HTML node tests
│   ├── test_textnode.py        # Text node tests
│   ├── test_inline_markdown.py # Inline markdown tests
│   ├── test_block_markdown.py  # Block markdown tests
│   └── test_markdown_to_html.py # Integration tests
├── main.sh                     # Application runner script
├── test.sh                    # Test runner script
├── CLAUDE.md                  # Claude Code guidance
└── README.md                  # Project documentation
```

## 🏗️ Architecture

### Core Components

#### TextNode Layer (`textnode.py`)
- **`TextNode`** - Represents text elements with type and optional URL
- **`TextType`** - Enum for different text types (text, bold, italic, code, links, images)
- **`text_node_to_html_node()`** - Converts TextNodes to HTMLNodes

#### HTMLNode Layer (`htmlnode.py`)
- **`HTMLNode`** - Base class with common interface and `props_to_html()` utility
- **`LeafNode`** - Terminal nodes with content (e.g., `<p>text</p>`, `<b>bold</b>`)
- **`ParentNode`** - Container nodes with children (e.g., `<div><span>content</span></div>`)

#### Inline Markdown Processing (`inline_markdown.py`)
- **`text_to_textnodes()`** - Main pipeline converting raw text to structured TextNodes
- **`split_nodes_delimiter()`** - Process inline formatting delimiters (**, *, `)
- **`extract_markdown_images()`** - Extract image references from markdown text
- **`extract_markdown_links()`** - Extract link references from markdown text

#### Block Markdown Processing (`block_markdown.py`)
- **`BlockType`** - Enum defining paragraph, heading, code, quote, unordered_list, ordered_list
- **`markdown_to_blocks()`** - Split markdown text into logical blocks
- **`block_to_block_type()`** - Classify markdown blocks by their type

#### Markdown-to-HTML Conversion (`markdown_to_html.py`)
- **`markdown_to_html_node()`** - Complete pipeline converting markdown documents to HTML node trees
- **`extract_title()`** - Extract h1 header from markdown documents for page titles

### Design Patterns

The architecture follows **SOLID principles** with clear separation of responsibilities:

- **Single Responsibility** - Each class has one reason to change
- **Open/Closed** - Easy to extend with new node types or text types
- **Inheritance Hierarchy** - HTMLNode → LeafNode/ParentNode
- **Composition** - TextNodes convert to HTMLNodes through dedicated functions

## 🚀 Quick Start

### Prerequisites

- Python 3.6+
- No external dependencies required

### Running the Application

```bash
# Using the shell script
./main.sh

# Or directly with Python
python3 src/main.py
```

### Running Tests

```bash
# Run all tests
./test.sh

# Or with Python unittest
python3 -m unittest discover -s src

# Run specific test files
python3 -m unittest src.test_textnode
python3 -m unittest src.test_htmlnode
python3 -m unittest src.test_inline_markdown
python3 -m unittest src.test_block_markdown
python3 -m unittest src.test_markdown_to_html
```

## 📝 Usage Examples

### Complete Markdown-to-HTML Conversion

```python
from markdown_to_html import markdown_to_html_node

# Convert complete markdown document
markdown = """# My Blog Post

This is a paragraph with **bold** and *italic* text.

## Code Example

```python
def hello():
    print("Hello, World!")
```

> This is a quote with some important information.

- First item
- Second item
- Third item
"""

# Convert to HTML node tree
html_node = markdown_to_html_node(markdown)

# Generate final HTML
html_output = html_node.to_html()
```

### Extracting Page Titles

```python
from markdown_to_html import extract_title

# Extract h1 header for page title
markdown = """# My Blog Post

This is the content of the blog post."""

title = extract_title(markdown)
# Result: "My Blog Post"

# Handles whitespace and formatting
title = extract_title("#   Welcome to My Site   ")
# Result: "Welcome to My Site"

# Raises exception if no h1 header found
try:
    title = extract_title("## Only h2 headers here")
except Exception as e:
    print("No h1 header found")
```

### Processing Inline Markdown

```python
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

# Process text with multiple inline formats
text = "This has **bold**, *italic*, and `code` formatting with a [link](https://example.com)"
text_nodes = text_to_textnodes(text)

# Convert to HTML nodes
html_nodes = [text_node_to_html_node(node) for node in text_nodes]
```

### Working with Block Types

```python
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

# Split markdown into blocks
markdown = """# Heading

Paragraph text here.

```
code block
```"""

blocks = markdown_to_blocks(markdown)
# Result: ["# Heading", "Paragraph text here.", "```\ncode block\n```"]

# Classify each block
for block in blocks:
    block_type = block_to_block_type(block)
    print(f"{block_type}: {block}")
# Output: BlockType.HEADING: # Heading
#         BlockType.PARAGRAPH: Paragraph text here.
#         BlockType.CODE: ```\ncode block\n```
```

## 🧪 Testing

The project includes comprehensive test coverage:

- **`test_textnode.py`** - TextNode functionality and text-to-HTML conversion
- **`test_htmlnode.py`** - HTML node hierarchy and generation
- **`test_inline_markdown.py`** - Inline markdown processing and extraction utilities
- **`test_block_markdown.py`** - Block-level markdown processing and classification
- **`test_markdown_to_html.py`** - Complete markdown-to-HTML conversion pipeline

### Test Categories

- ✅ **Unit Tests** - Individual component functionality
- ✅ **Integration Tests** - Component interaction testing
- ✅ **Edge Cases** - Boundary conditions and error handling
- ✅ **Validation Tests** - Input validation and error scenarios

## 🛠️ Development

### Code Patterns

- All classes implement `__eq__` and `__repr__` methods
- TextType enum uses string values for each type
- HTMLNode inheritance pattern with base class interface
- Properties converted to HTML attributes using `props_to_html()`
- Comprehensive error handling with descriptive messages

### Adding New Features

1. **New Text Types** - Add to `TextType` enum and update conversion logic
2. **New HTML Nodes** - Inherit from `HTMLNode` and implement `to_html()`
3. **New Markdown Features** - Add processing functions to `inline_markdown.py`
4. **Testing** - Add corresponding tests following existing patterns

## 📋 Roadmap

- [x] Full markdown parsing (headers, lists, paragraphs, quotes, code blocks)
- [x] Complete markdown-to-HTML conversion pipeline
- [x] Title extraction from markdown documents
- [x] Quote blocks with empty lines support
- [ ] File system integration for reading markdown files
- [ ] Template system for HTML generation
- [ ] CSS styling support
- [ ] Static file copying
- [ ] Build system for generating complete websites
- [ ] Configuration system for customization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following existing code patterns
4. Add tests for new functionality
5. Ensure all tests pass (`./test.sh`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Python's standard library
- Inspired by modern static site generators like Hugo and Jekyll
- Designed with clean architecture principles and testability in mind
