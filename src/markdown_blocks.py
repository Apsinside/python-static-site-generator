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