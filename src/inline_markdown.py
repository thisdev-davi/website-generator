from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = [] # final
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        parts = node.text.split(delimiter)
        if len(parts) == 1:
            result.append(node)
            continue
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter {delimiter}!")
        
        nodes = [] # temporary
        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part != "":
                    nodes.append(TextNode(part, TextType.TEXT))
            else:
                nodes.append(TextNode(part, text_type))
        result.extend(nodes)                
    return result

    
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches