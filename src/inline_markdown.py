from cgitb import text
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
        
        aux = [] # temporary
        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part != "":
                    aux.append(TextNode(part, TextType.TEXT))
            else:
                aux.append(TextNode(part, text_type))
        result.extend(aux)                
    return result

    
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_images(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        if not extract_markdown_images(node.text):
            result.append(node)
            continue
        
        remaining = node.text
        while True:
            parts = extract_markdown_images(remaining)
            if not parts:
                if remaining != "":
                    result.append(TextNode(remaining, TextType.TEXT))
                break

            alt, url = parts[0]
            string = f"![{alt}]({url})"
            before, after = remaining.split(string, 1)
            if before != "":
                result.append(TextNode(before, TextType.TEXT))
            result.append(TextNode(alt,TextType.IMAGE, url=url))
            remaining = after
    return result
            
def split_nodes_links(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        if not extract_markdown_links(node.text):
            result.append(node)
            continue
        
        remaining = node.text
        while True:
            parts = extract_markdown_links(remaining)
            if not parts:
                if remaining != "":
                    result.append(TextNode(remaining, TextType.TEXT))
                break

            alt, url = parts[0]
            string = f"[{alt}]({url})"
            before, after = remaining.split(string, 1)
            if before != "":
                result.append(TextNode(before, TextType.TEXT))
            result.append(TextNode(alt,TextType.LINK, url=url))
            remaining = after
    return result

def text_to_textnode(text):
    parts = [TextNode(text, TextType.TEXT)]
    parts = split_nodes_delimiter(parts, "`", TextType.CODE)
    parts = split_nodes_delimiter(parts, "**", TextType.BOLD)
    parts = split_nodes_delimiter(parts, "_", TextType.ITALIC)
    parts = split_nodes_images(parts)
    parts = split_nodes_links(parts)
    return parts

def markdown_to_block(markdown):
    split_text = markdown.split("\n\n")
    blocks = []
    for text in split_text:
        text = text.strip()
        if text == "":
            continue

        split_lines = text.split("\n")
        aux = []
        for p in split_lines:
            aux.append(p.strip())

        text = "\n".join(aux)
        blocks.append(text)
    return blocks