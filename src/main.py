from textnode import TextNode,TextType
from inline_markdown import split_nodes_delimiter
def main():
    text = "This is text with a **bolded word** and **another**"
    print(text.split("**"))
    node = TextNode(
        "This is text with a **bolded word** and **another**", TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print (new_nodes)

main()