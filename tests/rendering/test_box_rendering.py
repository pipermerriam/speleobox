from __future__ import unicode_literals

from speleobox.datastructures import Cell
from speleobox.rendering import (
    BLANK_CELL,
    render_box,
)


BLANK_LEVEL = (
    tuple("Level #1"),
    tuple("----------------------"),
    tuple("|         ||         |"),
    tuple("|         ||         |"),
    tuple("|         ||         |"),
    tuple("----------------------"),
    tuple("----------------------"),
    tuple("|         ||         |"),
    tuple("|         ||         |"),
    tuple("|         ||         |"),
    tuple("----------------------"),
    tuple("Level #2"),
    tuple("----------------------"),
    tuple("|         ||         |"),
    tuple("|         ||         |"),
    tuple("|         ||         |"),
    tuple("----------------------"),
    tuple("----------------------"),
    tuple("|         ||         |"),
    tuple("|         ||         |"),
    tuple("|         ||         |"),
    tuple("----------------------"),
)


def test_blank_box():
    box = [[
        [Cell(*((False,) * 6)) for _ in range(2)] for _ in range(2)
    ] for _ in range(2)]
    rendered_box = render_box(box)
    assert all(
        left == right for left, right in zip(rendered_box, BLANK_LEVEL)
    )

