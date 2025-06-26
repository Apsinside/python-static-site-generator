from textnode import TextNode,TextType, text_node_to_html_node
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, text_to_textnodes
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode, LeafNode

def text_to_children(text):
    children = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        node.text = node.text.replace("\n", "")
        children.append(text_node_to_html_node(node))

    return children

def code_to_html_node(text):
    text_node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([text_node], "`", TextType.CODE) 
    nodes[0].text = nodes[0].text[1:]   
    code_node = [text_node_to_html_node(nodes[0])]
    return ParentNode("pre", code_node)

def unordered_list_to_html_node(text):
    child_nodes = []
    for entry in text.split("-"):
        if entry:
            child_nodes.append(ParentNode("li", text_to_children(entry)))
    return child_nodes

def ordered_list_to_html_node(text):
    child_nodes = []
    for entry in text.split("\n"):
        if entry:
            child_nodes.append(ParentNode("li", text_to_children(entry.split(".", 1)[1])))
    return child_nodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match(block_type):
            case BlockType.PARAGRAPH:
                node = ParentNode("p", text_to_children(block))
                print(node)
            case BlockType.HEADING:
                header_depth = 0
                for char in block:
                        if char == "#":
                            header_depth += 1
                node = ParentNode(f"h{header_depth}", text_to_children(block[header_depth:]))
            case BlockType.CODE:  
                node = code_to_html_node(block)
            case BlockType.QUOTE:
                node = ParentNode("blockquote", text_to_children(block))
            case BlockType.UNORDERED_LIST:
                node = ParentNode("ul",unordered_list_to_html_node(block))
            case BlockType.ORDERED_LIST:
                node = ParentNode("ol",ordered_list_to_html_node(block))
        nodes.append(node)
    return ParentNode("div", nodes)

def main():
    md ="""
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    print(markdown_to_html_node(md).to_html())

    
main()