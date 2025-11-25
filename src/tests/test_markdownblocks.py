import unittest
from markdown.markdown_blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
                This is **bolded** paragraph

                This is another paragraph with _italic_ text and `code` here
                This is the same paragraph on a new line

                - This is a list
                - with items
            """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), "heading")
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), "code")
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), "quote")
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), "unordered_list")
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), "ordered_list")
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_markdown_to_html_node(self):
        markdown = """
# Heading

This is a paragraph with **bold** text.

* List item 1
* List item 2
"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertIn("<h1>Heading</h1>", html)
        self.assertIn("<p>This is a paragraph with <b>bold</b> text.</p>", html)
        self.assertIn("<ul><li>List item 1</li><li>List item 2</li></ul>", html)