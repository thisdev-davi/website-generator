import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Link", props={"href": " https://example.com ", "target": " _blank "})
        self.assertEqual(node.props_to_html(), "href=\"https://example.com\" target=\"_blank\"")

    def test_repr(self):
        node = HTMLNode(tag="a", value="Link", props={"href": " https://boot.dev ", "target": " _blank "})
        node2 = "Tag: a, Value: Link, Children: None, Props: href=\"https://boot.dev\" target=\"_blank\""
        self.assertEqual(repr(node), node2)
    
    def test_object_comparison(self):
        node = HTMLNode(tag="a", value="Link", props={"href": " https://boot.dev ", "target": " _blank "})
        self.assertIsInstance(node, HTMLNode)

if __name__ == "__main__":
    unittest.main()