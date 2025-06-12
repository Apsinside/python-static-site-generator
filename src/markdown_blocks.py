from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    if 6 > block[:5].count("#") >= 1:
        return BlockType.HEADING
    if block[:3] == "```" and block[len(block) - 3:] == "```":
        return BlockType.CODE
    if all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    if all(line.startswith("-") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST

    split_block = block.split("\n")
    ordered_list = False
    for i in range(0, len(split_block)):
        ordered_list = split_block[i].startswith(f"{i + 1}") and split_block[i][1:3] == ". "
    if(ordered_list):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = []
    for str in markdown.split("\n\n"):
        temp_blocks=[]
        for s in str.split("\n"):
            temp_blocks.append(s.strip())
        unstripped = "\n".join(temp_blocks)       
        if unstripped.startswith("\n"):
            unstripped = unstripped.lstrip("\n")
        if unstripped.endswith("\n"):
            unstripped = unstripped.rstrip("\n")
        blocks.append(unstripped)
        filtered_blocks = list(filter(None, blocks))
    return filtered_blocks

# def markdown_to_blocks(markdown):
#     blocks = markdown.split("\n\n")
#     filtered_blocks = []
#     for block in blocks:
#         if block == "":
#             continue
#         block = block.strip()
#         filtered_blocks.append(block)
#     return filtered_blocks