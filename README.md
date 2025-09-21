# Static Site Generator

A Python-based static site generator that converts markdown files to static websites with a clean, modular architecture.

## 🚀 Features

- **Text Processing Pipeline** - Clean separation between text representation and HTML generation
- **Markdown Support** - Extract and process markdown images and links
- **Inline Formatting** - Support for bold, italic, and code formatting with delimiter processing
- **Modular Architecture** - Well-structured codebase with clear separation of concerns
- **Comprehensive Testing** - Extensive test suite with 100+ test cases

## 📁 Project Structure

```
StaticSiteGenerator/
├── src/
│   ├── htmlnode.py          # HTML generation layer
│   ├── textnode.py          # Text representation layer
│   ├── inline_markdown.py   # Markdown processing utilities
│   ├── main.py             # Application entry point
│   ├── test_htmlnode.py    # HTML node tests
│   ├── test_textnode.py    # Text node tests
│   └── test_inline_markdown.py # Markdown processing tests
├── main.sh                 # Application runner script
├── test.sh                # Test runner script
└── README.md              # Project documentation
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

#### Markdown Processing (`inline_markdown.py`)
- **`split_nodes_delimiter()`** - Process inline formatting delimiters (**, *, `)
- **`extract_markdown_images()`** - Extract image references from markdown text
- **`extract_markdown_links()`** - Extract link references from markdown text

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
```

## 📝 Usage Examples

### Creating HTML from Text

```python
from textnode import TextNode, TextType, text_node_to_html_node

# Create a text node
text_node = TextNode("Hello World", TextType.BOLD)

# Convert to HTML node
html_node = text_node_to_html_node(text_node)

# Generate HTML
print(html_node.to_html())  # Output: <b>Hello World</b>
```

### Processing Markdown Delimiters

```python
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

# Create text with bold formatting
nodes = [TextNode("This has **bold** text", TextType.TEXT)]

# Process bold delimiters
result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

# Result: [TextNode("This has ", TEXT), TextNode("bold", BOLD), TextNode(" text", TEXT)]
```

### Extracting Markdown Elements

```python
from inline_markdown import extract_markdown_images, extract_markdown_links

# Extract images
text = "Check out this ![cool image](https://example.com/image.png)"
images = extract_markdown_images(text)
# Result: [("cool image", "https://example.com/image.png")]

# Extract links
text = "Visit [our website](https://example.com) for more info"
links = extract_markdown_links(text)
# Result: [("our website", "https://example.com")]
```

## 🧪 Testing

The project includes comprehensive test coverage:

- **`test_textnode.py`** - TextNode functionality and text-to-HTML conversion
- **`test_htmlnode.py`** - HTML node hierarchy and generation
- **`test_inline_markdown.py`** - Markdown processing and extraction utilities

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

- [ ] Full markdown parsing (headers, lists, paragraphs)
- [ ] File system integration for reading markdown files
- [ ] Template system for HTML generation
- [ ] CSS styling support
- [ ] Static file copying
- [ ] Build system for generating complete websites

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
