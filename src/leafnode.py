from htmlnode import HTMLNode

class LeafNode(HTMLNode):
        def __init__(self, tag, value, props=None):
            super().__init__(tag, value, children=None, props=props)

        def to_html(self):
            props = "" if not self.props else " " + self.props_to_html()
            if self.value is None:
                raise ValueError("All leaf nodes must have a value!")
            if self.tag is None:
                return f"{self.value}"
            
            tag = self.tag.strip()
            value = self.value.strip()
            return f"<{tag}{props}>{value}</{tag}>"