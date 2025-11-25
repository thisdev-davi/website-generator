import unittest
from nodes.parentnode import ParentNode
from nodes.leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_siblings(self):
        sibling_node1 = LeafNode("p", "sibling1")
        sibling_node2 = LeafNode("p", "sibling2")
        parent_node = ParentNode("div", [sibling_node1, sibling_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p>sibling1</p><p>sibling2</p></div>",
        )