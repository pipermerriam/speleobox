from __future__ import unicode_literals

import copy

from speleobox.datastructures import Cell
from speleobox.rendering import (
    BLANK_CELL,
    render_line,
)


BLANK_LINE = (
    tuple("---------------------------------"),
    tuple("|         ||         ||         |"),
    tuple("|         ||         ||         |"),
    tuple("|         ||         ||         |"),
    tuple("---------------------------------"),
)


def test_blank_line():
    line = map(copy.deepcopy,
        (Cell(*((False,) * 6)) for i in range(3))
    )
    rendered_line = render_line(line)
    assert all(
        left == right for left, right in zip(rendered_line, BLANK_LINE)
    )
