from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            if block.startswith("# "):
                return block[2:].strip()

    raise Exception("No h1 header found")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    per_block = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(block)
            children = [text_node_to_html_node(text_node) for text_node in text_nodes]
            per_block.append(ParentNode("p", children))
        
        if block_type == BlockType.CODE:
            lines = block.split("\n")
            inner_lines = lines[1:-1]
            inner_text = "\n".join(inner_lines) + "\n"
            code_node = LeafNode("code", inner_text)
            per_block.append(ParentNode("pre", [code_node]))
        
        if block_type == BlockType.HEADING:
            tokens, text = (block.split(maxsplit=1) + [""])[:2]
            num_headings = len(tokens) if set(tokens) == {"#"} and 1 <= len(tokens) <= 6 else 1
            text_nodes = text_to_textnodes(text)
            children = [text_node_to_html_node(text_node) for text_node in text_nodes]
            per_block.append(ParentNode(f"h{num_headings}", children))
        
        if block_type == BlockType.UNORDERED_LIST:
            li_nodes = []
            for line in block.splitlines():
                if line.startswith("- ") or line.startswith("* "):
                    item_text = line[2:]
                    text_nodes = text_to_textnodes(item_text)
                    li_children = [text_node_to_html_node(tn) for tn in text_nodes]
                    li_nodes.append(ParentNode("li", li_children))
            per_block.append(ParentNode("ul", li_nodes))
        
        if block_type == BlockType.ORDERED_LIST:
            li_nodes = []
            for line in block.splitlines():
                i = 0
                while i < len(line) and line[i].isdigit():
                    i += 1
                if i > 0 and line[i:i+2] == ". ":
                    item_text = line[i+2:]
                    text_nodes = text_to_textnodes(item_text)
                    li_children = [text_node_to_html_node(tn) for tn in text_nodes]
                    li_nodes.append(ParentNode("li", li_children))
            per_block.append(ParentNode("ol", li_nodes))

        if block_type == BlockType.QUOTE:
            lines = block.splitlines()
            quote_lines = []
            for line in lines:
                if line.startswith("> "):
                    quote_lines.append(line[2:])
                elif line == ">":
                    quote_lines.append("")
            text = "\n".join(quote_lines)
            text_nodes = text_to_textnodes(text)
            children = [text_node_to_html_node(tn) for tn in text_nodes]
            per_block.append(ParentNode("blockquote", children))
                    


    return ParentNode("div", per_block)