from textnode import TextNode, TextType
from htmlnode import HTMLNode

text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
print(text_node.__repr__())
html_node = HTMLNode("a", "This is some anchor text", props={"href": " https://www.boot.dev ", "target": " _blank "})
print(html_node.__repr__())
print(html_node.props_to_html())