from enum import Enum

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

    def __eq__(self, text):
        if self.text == text and self.text_type == text.text_type and self.url == text.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text_type}, {self.text_type.value}, {self.url})"