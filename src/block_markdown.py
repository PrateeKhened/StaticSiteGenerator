import enum

class BlockType(enum.Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(headings):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    

    if block.startswith("1. "):
        i = 1 
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):

    blocks = markdown.split("\n\n")

    stripped_blocks = []
    for block in blocks:
        splitted = block.split("\n")
        stripped_blocks.append("\n".join(line.strip() for line in splitted))

    final_blocks = []
    for block in stripped_blocks:
        if block:
            final_blocks.append(block.strip("\n"))

    return final_blocks