import pathlib
import unittest

from tile.tree_algorithms import parse


class TestSum(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        input_path = pathlib.Path("tests/data/end_to_end_input")
        output_path = pathlib.Path("tests/data/end_to_end_output")
        with input_path.open() as f:
            cls.input_lines = f.readlines()
        with output_path.open() as f:
            cls.output = set(line.strip() for line in f.readlines())

    def test_end_to_end(self):
        output = set(parse(self.input_lines))
        assert output == self.output
