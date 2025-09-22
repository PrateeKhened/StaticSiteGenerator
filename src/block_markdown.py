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