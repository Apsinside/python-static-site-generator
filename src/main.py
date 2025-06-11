from textnode import TextNode,TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
import re

def main():
    md ="""
    This is **bolded** paragraph




    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    blocks = md.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    print(blocks)

main()