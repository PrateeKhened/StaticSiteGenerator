# Static Site Generator

A Python-based static site generator that converts markdown files into beautiful static websites with zero dependencies.

## Description

This static site generator transforms your markdown content into a complete website using a clean, modular architecture. It features:

- **Full Markdown Support** - Headings, paragraphs, code blocks, quotes, lists, bold, italic, links, and images
- **Template System** - Simple HTML templates with placeholder replacement
- **Asset Management** - Automatic copying of static files (CSS, images, etc.)
- **Development Server** - Built-in local server for testing your site
- **Zero Dependencies** - Uses only Python standard library
- **Comprehensive Testing** - 130+ test cases ensuring reliability

## Motivation

Modern static site generators often come with complex dependencies, steep learning curves, and opinionated frameworks. This project provides a simple, educational approach to static site generation that:

- **Teaches fundamentals** - Clear, readable code that demonstrates how static site generators work
- **Stays lightweight** - No external dependencies or complex configuration
- **Remains flexible** - Easy to understand and modify for specific needs
- **Follows best practices** - Clean architecture with proper separation of concerns

## Quick Start

### Prerequisites

- Python 3.6+
- No external dependencies required

### Installation

1. Clone the repository:
```bash
git clone https://github.com/prateekkhenedcodes/StaticSiteGenerator.git
cd StaticSiteGenerator
```

2. Create your content structure:
```
your-site/
├── content/           # Your markdown files
│   ├── index.md
│   └── about.md
├── static/            # CSS, images, etc.
│   └── style.css
└── template.html      # HTML template
```

3. Create a simple template (`template.html`):
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ Title }}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    {{ Content }}
</body>
</html>
```

4. Generate your site and start the development server:
```bash
./main.sh
```

Your site will be available at `http://localhost:8888`

### Example Content

Create `content/index.md`:
```markdown
# Welcome to My Site

This is a **static site** generated from *markdown*!

## Features

- Easy to use
- Fast generation
- Clean output

Check out the [about page](about.html)!
```

## Usage

### Basic Commands

**Generate site and start development server:**
```bash
./main.sh
```

**Generate site only:**
```bash
python3 src/main.py
```

**Run tests:**
```bash
./test.sh
```

### Project Structure

Your site should follow this structure:
```
StaticSiteGenerator/
├── content/              # Markdown files (.md)
├── static/               # CSS, images, assets
├── template.html         # HTML template
├── docs/                 # Generated output
└── src/                  # Generator source code
```

### Template System

Templates use simple placeholder replacement:
- `{{ Title }}` - Replaced with the h1 heading from markdown
- `{{ Content }}` - Replaced with the generated HTML content

### Supported Markdown Features

- **Headings** - `# ## ###` (h1, h2, h3)
- **Text formatting** - `**bold**`, `*italic*`, `` `code` ``
- **Links** - `[text](url)`
- **Images** - `![alt](url)`
- **Lists** - `- item` and `1. item`
- **Code blocks** - `` ``` code ``` ``
- **Quotes** - `> quote text`

## Contributing

We welcome contributions! Here's how to get started:

### Development Setup

1. **Fork and clone** the repository
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Make your changes** following the existing code patterns
4. **Add tests** for new functionality in the `src/test_*.py` files
5. **Run the test suite**: `./test.sh` (ensure all tests pass)
6. **Test the generator**: `./main.sh` (verify the site builds correctly)

### Code Guidelines

- **Follow existing patterns** - All classes implement `__eq__` and `__repr__` methods
- **Write tests** - Each new feature should include comprehensive test coverage
- **Use descriptive names** - Functions and variables should clearly express their purpose
- **Keep it simple** - Favor readable code over clever optimizations
- **Test edge cases** - Include tests for boundary conditions and error scenarios

### Running Tests

```bash
# Run all tests
./test.sh

# Run specific test files
python3 -m unittest src.test_textnode
python3 -m unittest src.test_markdown_to_html

# Run individual test classes
python3 -m unittest src.test_block_markdown.TestBlockToBlockType
```

### Submitting Changes

1. **Commit your changes**: `git commit -m 'Add amazing feature'`
2. **Push to your fork**: `git push origin feature/your-feature`
3. **Create a Pull Request** with a clear description of your changes

### Areas for Contribution

- **New markdown features** (tables, strikethrough, etc.)
- **Performance optimizations**
- **Additional template features**
- **Better error messages**
- **Documentation improvements**

---

**License**: MIT License
**Built with**: Python standard library only
