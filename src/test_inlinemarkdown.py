import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_links, text_to_textnode

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        nodes = [
            TextNode("This is a **bold** text", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)
    
    def test_split_nodes_delimiter_italic(self):
        nodes = [
            TextNode("This is an _italic_ text", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        expected = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://boot.dev)")
        self.assertListEqual([("link", "https://boot.dev")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and another [second link](https://boot.dev/second)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://boot.dev/second"),
            ],
            new_nodes,
        )

    def test_convert_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_textnode(text)

        self.assertEqual(len(text_nodes), 10)
        self.assertEqual(text_nodes[0], TextNode("This is ", TextType.TEXT))
        self.assertEqual(text_nodes[1], TextNode("text", TextType.BOLD))
        self.assertEqual(text_nodes[2], TextNode(" with an ", TextType.TEXT))
        self.assertEqual(text_nodes[3], TextNode("italic", TextType.ITALIC))
        self.assertEqual(text_nodes[4], TextNode(" word and a ", TextType.TEXT))
        self.assertEqual(text_nodes[5], TextNode("code block", TextType.CODE))
        self.assertEqual(text_nodes[6], TextNode(" and an ", TextType.TEXT))
        self.assertEqual(text_nodes[7], TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"))
        self.assertEqual(text_nodes[8], TextNode(" and a ", TextType.TEXT))
        self.assertEqual(text_nodes[9], TextNode("link", TextType.LINK, "https://boot.dev"))