#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from i3bindings import *


class TestBindingsParser(unittest.TestCase):
    def test_find(self):
        x = "x"
        self.assertEqual(find("", x), -1)
        self.assertEqual(find("\n", x), -1)
        self.assertEqual(find("line without X", x), -1)
        self.assertEqual(find("line with x", x), 10)
        self.assertEqual(find("line with xxxxxxxs", x), 10)

    def test_format(self):
        key = "x"
        cmd = "y"
        cmd_type = TYPE_EXEC
        f = format_line
        self.assertEqual(f((key, cmd), cmd_type), " ".join([BINDSYM, key, EXEC, cmd]))
        cmd_type = TYPE_BIND
        self.assertEqual(f((key, cmd), cmd_type), " ".join([BINDSYM, key, cmd]))

    def test_extract_dashed(self):
        f = extract_dashed
        self.assertEqual(f("Shift"), ["Shift"])
        self.assertEqual(f("1-5"), ["1", "2", "3", "4", "5"])

    def test_extract_bracketed(self):
        f = extract_bracketed
        self.assertEqual(f("startend"), ("startend", "", []))
        self.assertEqual(f("start{}end"), ("start", "end", []))
        self.assertEqual(f("start{xy}end"), ("start", "end", ["xy"]))
        self.assertEqual(f("start{x,y}end"), ("start", "end", ["x", "y"]))
        self.assertEqual(f("{x,y}end"), ("", "end", ["x", "y"]))
        self.assertEqual(f("start{x,y}"), ("start", "", ["x", "y"]))
        self.assertEqual(f("start{x,y}end{}"), ("start", "end{}", ["x", "y"]))
        self.assertEqual(f("{,y}"), ("", "", ["", "y"]))
        self.assertEqual(f("{,,,}"), ("", "", ["", "", "", ""]))
        self.assertEqual(f("{,x/y}"), ("", "", ["", "x/y"]))
        self.assertEqual(f("{,x/y,1-3}"), ("", "", ["", "x/y", "1", "2", "3"]))

    def test_extract_slashed(self):
        f = extract_slashed
        self.assertEqual(f("startend"), ("", "startend", []))
        self.assertEqual(f("start end"), ("start ", "end", []))
        self.assertEqual(f("start/end"), ("", "", ["start", "end"]))
        self.assertEqual(f("x y z start/end"), ("x y z ", "", ["start", "end"]))
        self.assertEqual(f("start/end 1 2 3"), ("", " 1 2 3", ["start", "end"]))
        self.assertEqual(f("asd / asv"), ("asd ", "/ asv", []))
        self.assertEqual(f("$mod+h/Left"), ("$mod+", "", ["h", "Left"]))

    def test_split_line(self):
        f = split_line
        self.assertEqual(f(""), None)
        self.assertEqual(f("xyz asdf"), None)
        self.assertEqual(f("xyz:asdf"), ("xyz", "asdf", TYPE_BIND))
        self.assertEqual(f("xyz   :    asdf"), ("xyz", "asdf", TYPE_BIND))
        self.assertEqual(f("xyz:asdf::x"), ("xyz", "asdf::x", TYPE_BIND))
        self.assertEqual(f("xyz::asdf"), ("xyz", "asdf", TYPE_EXEC))
        self.assertEqual(f("xyz    ::            asdf"), ("xyz", "asdf", TYPE_EXEC))
        self.assertEqual(f("xyz::asdf:x"), ("xyz", "asdf:x", TYPE_EXEC))
        self.assertEqual(
            f("$mod+Control+Shift+h/Left : resize shrink width 5px or 5ppt"),
            ("$mod+Control+Shift+h/Left", "resize shrink width 5px or 5ppt", TYPE_BIND),
        )

    def test_filter_line(self):
        f = filter_line
        self.assertEqual(f(""), False)
        self.assertEqual(f("\n"), False)
        self.assertEqual(f("      "), False)
        self.assertEqual(f("# Comment"), False)
        self.assertEqual(f("# Comment:"), False)
        self.assertEqual(f(":"), True)
        self.assertEqual(f("abc : def"), True)

    def test_parse_command(self):
        f = parse_command
        self.assertEqual(f(("", "")), [("", "")])
        self.assertEqual(f(("xyz", "abc")), [("xyz", "abc")])
        self.assertEqual(f(("x/y", "abc")), [("x", "abc"), ("y", "abc")])
        self.assertEqual(f(("{x,y}", "{a,b}")), [("x", "a"), ("y", "b")])
        self.assertEqual(f(("{x,y}", "{}")), [])
        self.assertEqual(f(("{x,y}", "{z}")), [])


if __name__ == "__main__":
    unittest.main()
