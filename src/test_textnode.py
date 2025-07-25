import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    # Tests to see if two nodes are equal
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    # Tests to see if text type is not equal
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a link node", TextType.LINK)
        self.assertNotEqual(node, node2)
    # Tests to see if url is not equal
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, 'https://test.com')
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()