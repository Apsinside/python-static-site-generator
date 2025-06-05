from textnode import TextNode,TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from extract_markdown import 
def main():
    img_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    link_text= "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotde)"
    print(extract_markdown_images(img_text))
    print(extract_markdown_images(link_text))
    print(extract_markdown_links(img_text))
    print(extract_markdown_links(link_text))
main()