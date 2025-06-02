import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_all_eq(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual (node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual (node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a link node", TextType.LINK, "")
        self.assertNotEqual (node, node2)

    def test_all_not_eq(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual (node, node2)

if __name__ == "__main__":
    unittest.main()