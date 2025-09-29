class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("")

    def props_to_html(self):
        href = self.props.get("href").strip()
        target = self.props.get("target").strip()
        return f"href=\"{href}\" target=\"{target}\""

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props_to_html()}"