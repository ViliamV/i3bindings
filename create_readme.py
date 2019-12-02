#!/usr/bin/env python
import collections
import pathlib
import re

from tile.tree_algorithms import parse


TEMPLATE_FILE = pathlib.Path("./README-TEMPLATE.md")
EXAMPLES_FILE = pathlib.Path("./README-EXAMPLES.txt")
OUTPUT_FILE = pathlib.Path("./README.md")


def create_example(lines, outfile):
    input_lines = "\n".join(lines)
    output_lines = "\n".join(parse(lines))
    outfile.write(f"```css\nINPUT:\n{input_lines}\n\nOUTPUT:\n{output_lines}\n```\n")


def main():
    # Load examples
    examples = collections.defaultdict(list)
    with EXAMPLES_FILE.open() as f:
        for line in f:
            match = re.match("(\d+):", line)
            if match:
                key = match.groups()[0]
            else:
                if not key:
                    raise NotImplementedError
                examples[key].append(line.strip())
    with TEMPLATE_FILE.open() as infile, OUTPUT_FILE.open("w") as outfile:
        for line in infile:
            match = re.match("example:(\d+)", line)
            if match:
                key = match.groups()[0]
                if not key in examples:
                    raise NotImplementedError
                create_example(examples[key], outfile)
            else:
                outfile.write(line)


if __name__ == "__main__":
    main()
