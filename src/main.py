from textnode import TextNode,TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
import re

def main():
    block = "```this is some code```"
    print(block[1:2])
    print(block[len(block) - 3:])

main()