from textnode import TextNode
from textnode import TextType

text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
print(text_node.__repr__())