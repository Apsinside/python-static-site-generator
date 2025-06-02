import unittest

from htmlnode import HTMLNode
from sys import stdout
from io import StringIO

class TestHTMLNode(unittest.TestCase):
    def test_print_to_html1(self):
        node = HTMLNode("<h>", "hi",None, {"href": "https://www.google.com", "target": "_blank"})
        html_props = node.props_to_html()
        self.assertEqual(html_props, " href=\"https://www.google.com\" target=\"_blank\"")

    def test_print_to_html2(self):
        node = HTMLNode("<h>", "hi",None, {"href": "https://www.google.com"})
        html_props= node.props_to_html()
        self.assertEqual(html_props, " href=\"https://www.google.com\"")

    def test_print_to_html3(self):
        node = HTMLNode("<h>", "hi",None, {"href": "https://www.google.com", "target": "_blank", "test" : "prop"})
        html_props = node.props_to_html()
        self.assertEqual(html_props, " href=\"https://www.google.com\" target=\"_blank\" test=\"prop\"")

    def test_print_HTMLNode(self):
        node = HTMLNode("<h>", "hi",None, {"href": "https://www.google.com"})   
        with StringIO() as output:
            print(node, file=output)
            contents = output.getvalue()
        self.assertEqual(contents, "HTMLNode(<h>, hi, None, {'href': 'https://www.google.com'})\n")

if __name__ == "__main__":
    unittest.main()