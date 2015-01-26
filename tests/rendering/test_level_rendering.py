from __future__ import unicode_literals

import copy

from speleobox.datastructures import Cell
from speleobox.rendering import (
    BLANK_CELL,
    render_level,
)


BLANK_LEVEL = (
    tuple("---------------------------------"),
    tuple("|         ||         ||         |"),
    tuple("|         ||         ||         |"),
    tuple("|         ||         ||         |"),
    tuple("---------------------------------"),
    tuple("---------------------------------"),
    tuple("|         ||         ||         |"),
    tuple("|         ||         ||         |"),
    tuple("|         ||         ||         |"),
    tuple("---------------------------------"),
    tuple("---------------------------------"),
    tuple("|         ||         ||         |"),
    tuple("|         ||         ||         |"),
    tuple("|         ||         ||         |"),
    tuple("---------------------------------"),
)


def test_blank_level():
    level = [[Cell(*((False,) * 6)) for _ in range(3)] for _ in range(3)]
    rendered_level = render_level(level)
    assert all(
        left == right for left, right in zip(rendered_level, BLANK_LEVEL)
    )
