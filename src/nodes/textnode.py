from enum import Enum
from nodes.leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_text):
        if not isinstance(other_text, TextNode):
            return False
        return (
            self.text == other_text.text and
            self.text_type == other_text.text_type and
            self.url == other_text.url
        )

    # tag, value, props
    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode(None, self.text)
        if self.text_type == TextType.BOLD:
            return LeafNode("b", self.text)
        if self.text_type == TextType.ITALIC:
            return LeafNode("i", self.text)
        if self.text_type == TextType.CODE:
            return LeafNode("code", self.text)
        if self.text_type == TextType.LINK:
            return LeafNode("a", self.text, props={"href": self.url})
        if self.text_type == TextType.IMAGE:
            return LeafNode("img", "", props={"src": self.url, "alt": self.text})
        raise ValueError(f"Invalid TextType!")