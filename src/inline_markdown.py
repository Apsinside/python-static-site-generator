from textnode import TextNode, TextType
import re

# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes =[]
#     for node in old_nodes:
#         if node.text_type is not TextType.TEXT:
#             new_nodes.append(node)
#             continue
        
#         inline_texts = []
#         for word in node.text.split(" "):
#             delimiter_idx = word.find(delimiter)
#             if delimiter_idx >= 0 and word.find(delimiter,delimiter_idx + len(delimiter)) == -1:
#                 raise Exception(f"TextNode node{node} is missing the closing {delimiter}")
#             inline_texts.append(word[delimiter_idx + len(delimiter):word.find(delimiter,delimiter_idx + len(delimiter))])

#         inline_idx = 0  
#         for text in node.text.split(delimiter):
#             if text == "":
#                 continue
#             if text not in inline_texts:
#                 new_nodes.append(TextNode(text, TextType.TEXT))
#             else:
#                 new_nodes.append(TextNode(inline_texts[inline_idx], text_type))
#                 inline_idx += 1
         
#     return new_nodes

# def split_keep_delimiter(text, delimiter):
#     parts = text.split(delimiter)
#     result = []
    
#     for i, part in enumerate(parts):
#         if i > 0:  # Add delimiter before each part except the first
#             result.append(delimiter)
#         result.append(part)
    
#     return result

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text) 
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text) 
    return matches