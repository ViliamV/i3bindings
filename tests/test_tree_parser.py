#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

import tile.constants as c
import tile.node as node
import tile.tree_parser as tree_parser


class TestSum(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = tree_parser.Parser()

    def setUp(self):
        self.root = node.Node(node.N.ROOT, node_data=c.COMMAND_MAPPING)
        self.left = node.Node(node.N.ROOT_CHILD, self.root)
        self.right = node.Node(node.N.ROOT_CHILD, self.root)

    def test_basic_parsing(self):
        sentance = ""
        with self.assertRaises(tree_parser.ParsingError):
            self.parser.parse(sentance)
        node.Node(node.N.TEXT, self.left, "foo")
        sentance = f"foo{c.COMMAND_MAPPING}"
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse one word")
        node.Node(node.N.TEXT, self.left, c.SPACE)
        node.Node(node.N.TEXT, self.left, "bar")
        sentance = f"foo bar{c.COMMAND_MAPPING}"
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse two words")
        node.Node(node.N.TEXT, self.left, c.SPACE)
        sentance = f"foo bar {c.COMMAND_MAPPING}"
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse space as word")
        node.Node(node.N.TEXT, self.left, c.SPACE)
        sentance = f"foo bar  {c.COMMAND_MAPPING}"
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse spaces as words")

    def test_split_parsing(self):
        sentance = c.COMMAND_MAPPING
        self.assertEqual(self.root, self.parser.parse(sentance), "Should split sentance")
        node.Node(node.N.TEXT, self.left, "foo")
        sentance = f"foo{c.COMMAND_MAPPING}"
        self.assertEqual(self.root, self.parser.parse(sentance), "Should split after word")
        node.Node(node.N.TEXT, self.right, "bar")
        sentance = f"foo{c.COMMAND_MAPPING}bar"
        self.assertEqual(self.root, self.parser.parse(sentance), "Should put words after split")
        node.Node(node.N.TEXT, self.right, c.SPACE)
        node.Node(node.N.TEXT, self.right, c.COMMAND_MAPPING)
        sentance = f"foo{c.COMMAND_MAPPING}bar {c.COMMAND_MAPPING}"
        self.assertEqual(self.root, self.parser.parse(sentance), "Should ignore next split")

    def test_paren_parsing(self):
        sentance = f"(){c.COMMAND_MAPPING}"
        self.assertEqual(self.root, self.parser.parse(sentance), "Should ignore empty parens")
        sentance = f"()(a){c.COMMAND_MAPPING}"
        node.Node(node.N.TEXT, self.left, "a")
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse non-empty parens")
        sentance = f"()(a)(b c){c.COMMAND_MAPPING}"
        node.Node(node.N.TEXT, self.left, "b c")
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse multi-word parens")
        sentance = f"()(a)(b c)((d)){c.COMMAND_MAPPING}"
        node.Node(node.N.TEXT, self.left, "d")
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse nested parens")
        sentance = f"()(a)(b c)((d))((e)f){c.COMMAND_MAPPING}"
        node.Node(node.N.TEXT, self.left, "e")
        node.Node(node.N.TEXT, self.left, "f")
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse composed parens")

    def test_alternatives(self):
        sentance = c.SLASH
        with self.assertRaises(tree_parser.ParsingError):
            self.parser.parse(sentance)
        sentance = f"a/b{c.COMMAND_MAPPING}"
        alt = node.Node(node.N.ALTERNATIVE, self.left, "a/b")
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse simple alternative")
        sentance = f"a/b/c{c.COMMAND_MAPPING}"
        alt.data = "a/b/c"
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse triple alternative")
        sentance = f"(a / b / c d){c.COMMAND_MAPPING}"
        alt.data = "a / b / c d"
        self.assertEqual(self.root, self.parser.parse(sentance), "Should parse alternative with spaces in parenthesis")


if __name__ == "__main__":
    unittest.main(verbosity=2)
