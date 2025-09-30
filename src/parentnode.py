from leafnode import LeafNode
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        props = "" if not self.props else " " + self.props_to_html()

        if self.tag is None:
            raise ValueError("All parent nodes must have a tag!")
        if self.children is None:
            raise ValueError("All parent nodes must have children!")
        
        child_html = ""
        for child in self.children:
            child_html += child.to_html()

        return f"<{self.tag}{props}>{child_html}</{self.tag}>"