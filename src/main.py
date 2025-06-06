from textnode import TextNode,TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
import re

def main():
    img_text = "This ![image](https://i.imgur.com/zjjcJKZ.png) is an image"
    link_text= "This is text with a link [to boot dev](https://www.boot.dev"

    split_img_text = re.split(r"(?<!!)\[(.*?)\]\((.*?)\)", link_text)
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", link_text)

    print(split_img_text)
    print(matches)

main()