from __future__ import unicode_literals

import itertools
import copy
from StringIO import StringIO

from speleobox.datastructures import (
    IN,
    OUT,
)


TRANSITIONS = (
    "\u2603",  # Snowman
    "\u2661",  # Heart
    "\u2605",  # Star
    "\u265e",  # Chess Knight
    "\u262f",  # Yin Yang
    "\u2622",  # Radiation
    "\u2744",  # Snowflake
    "\u266b",  # Music Note
    "\u2602",  # Umbrella
    "\u2740",  # Flower
    "\u2618",  # Shamrock
    "\U0001f337",  # Tulip
    "\U0001f40c",  # Snail
    "\U0001f40d",  # Snake
    "\U0001f41c",  # Snake
    "\U0001f422",  # Turtle
)

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

'''
    front
  012345678
 0-----------
 1|    ^    |
 2| < UxD > |
 3|    v    |
  -----------
     back
'''

BLANK_CELL = (
    list("-----------"),
    list("|         |"),
    list("|         |"),
    list("|         |"),
    list("-----------"),
)


def render_cell(cell):
    left, right, top, bottom, front, back = cell
    lines = copy.deepcopy(BLANK_CELL)
    if left:
        lines[1][0] = ' '
        lines[2][0] = ' '
        lines[3][0] = ' '
        if left == IN:
            lines[2][2] = RIGHT
        elif left == OUT:
            lines[2][2] = LEFT
    if right:
        lines[1][10] = ' '
        lines[2][10] = ' '
        lines[3][10] = ' '
        if right == IN:
            lines[2][8] = LEFT
        elif right == OUT:
            lines[2][8] = RIGHT
    if back:
        lines[4][1] = ' '
        lines[4][2] = ' '
        lines[4][3] = ' '
        lines[4][4] = ' '
        lines[4][5] = ' '
        lines[4][6] = ' '
        lines[4][7] = ' '
        lines[4][8] = ' '
        lines[4][9] = ' '
        if back == IN:
            lines[3][5] = UP
        elif back == OUT:
            lines[3][5] = DOWN
    if front:
        lines[0][1] = ' '
        lines[0][2] = ' '
        lines[0][3] = ' '
        lines[0][4] = ' '
        lines[0][5] = ' '
        lines[0][6] = ' '
        lines[0][7] = ' '
        lines[0][8] = ' '
        lines[0][9] = ' '
        if front == IN:
            lines[1][5] = DOWN
        elif front == OUT:
            lines[1][5] = UP
    if top and bottom:
        lines[2][4] = "U"
        lines[2][6] = "D"
    elif top:
        lines[2][5] = "U"
    elif bottom:
        lines[2][5] = "D"
    return lines


def render_line(line):
    cells = map(render_cell, line)
    return tuple(map(tuple, map(
        itertools.chain.from_iterable,
        zip(*cells),
    )))


def render_level(level):
    return tuple(itertools.chain.from_iterable(map(render_line, level)))


def render_box(box):
    rendered_levels = map(render_level, box)
    headings = [
        (tuple("Level #{0}".format(n + 1)),) for n in range(len(rendered_levels))
    ]
    return tuple(itertools.chain.from_iterable(
        itertools.chain.from_iterable(zip(headings, rendered_levels))
    ))


def print_lines(lines):
    print("\n".join(map("".join, lines)))


def print_box(box):
    print_lines(render_box(box))
