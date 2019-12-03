# tile
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/no-ragrets.svg)](https://forthebadge.com)

Syntax and config generator for tiling window managers.

## TL;DR
If you are using [i3](https://i3wm.org/) or [Sway](https://swaywm.org/)
check out the [example](#Example) below.

## Installation
`pip install tile`

## Usage
1. Create *input_file* using [Concepts](#Concepts) below.
2. Try it with `tile input_file`
3. Write it to i3 config using `tile --write input_file`
4. Write it to Sway config using `tile --write --sway input_file`

Check out `tile --help` for more options.

## Concepts
### Mapping types
*tile* supports two types of mappings:
1. Command bindings for WM built-in commands:
example:0
2. Exec bindings, which are self-explanatory
example:1

### Alternatives
*Alternatives* express the idea that the same action should be bound to multiple key-bindings.

For example:

example:2

### Variables
*Variables* are shorter way to write bindings that have a similar structure.

E.g.:
example:3

#### Range expansion
Inside variables you can write `1-10` and it will be expanded to `1,2,3...`.
example:4

#### Variable reference
You can reference current value of the variable using `@n` syntax, where `n` is the variable index.
Every variable is numbered (starting from 0) from left to right. E.g.:
```
foo {bar,{foo,bar}} {0-1} ...
    ^    ^          ^
    0    1          2
```

Use it like this:
example:5

Or to avoid repeating long sequences:

example:6

#### Empty value
You can use empty value inside *Variable*, denoted by `_`. E.g.
example:7

### Nesting
You can use *Alternatives* and *Variables* inside *Variable* to create many bindings at once.
example:8

## Additional syntax
### Parenthesis
By default, special characters like space, plus sign, etc. are *token* separators.
example:9
You can use parenthesis to modify the behavior:
example:10

### Comments
Empty lines or lines starting with `#` will be ignored.
example:11

## Example
example:12

## Background
[i3](https://i3wm.org/) is a great windows manager but its config is pretty verbose.
I tried [bspwm](https://github.com/baskerville/bspwm) with its hotkey daemon [sxhkd](https://github.com/baskerville/sxhkd) and I much prefer that syntax.
That's why I wrote *tile*.
