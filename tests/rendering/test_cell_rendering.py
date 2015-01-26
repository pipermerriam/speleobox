from __future__ import unicode_literals

from speleobox.datastructures import (
    IN,
    OUT,
    Cell,
)
from speleobox.rendering import (
    BLANK_CELL,
    render_cell,
)


def test_blank_cell():
    cell = Cell(False, False, False, False, False, False)
    rendered =  render_cell(cell)
    assert rendered == BLANK_CELL


def test_open_left():
    cell = Cell(
        left=OUT,
        right=False,
        front=False,
        back=False,
        top=False,
        bottom=False,
    )
    expected = (
        list("-----------"),
        list("          |"),
        list("  <       |"),
        list("          |"),
        list("-----------"),
    )
    rendered = render_cell(cell)
    assert all(left == right for left, right in zip(rendered, expected))


def test_open_right():
    cell = Cell(
        left=False,
        right=OUT,
        front=False,
        back=False,
        top=False,
        bottom=False,
    )
    expected = (
        list("-----------"),
        list("|          "),
        list("|       >  "),
        list("|          "),
        list("-----------"),
    )
    rendered = render_cell(cell)
    assert all(left == right for left, right in zip(rendered, expected))


def test_open_front():
    cell = Cell(
        left=False,
        right=False,
        front=OUT,
        back=False,
        top=False,
        bottom=False,
    )
    expected = (
        list("-         -"),
        list("|    ^    |"),
        list("|         |"),
        list("|         |"),
        list("-----------"),
    )
    rendered = render_cell(cell)
    assert all(left == right for left, right in zip(rendered, expected))


def test_open_back():
    cell = Cell(
        left=False,
        right=False,
        front=False,
        back=OUT,
        top=False,
        bottom=False,
    )
    expected = (
        list("-----------"),
        list("|         |"),
        list("|         |"),
        list("|    v    |"),
        list("-         -"),
    )
    rendered = render_cell(cell)
    assert all(left == right for left, right in zip(rendered, expected))


def test_lateral_directions():
    cell = Cell(
        left=OUT,
        right=OUT,
        front=OUT,
        back=OUT,
        top=False,
        bottom=False,
    )
    rendered =  render_cell(cell)
    assert rendered[2][2] == '<'
    assert rendered[2][8] == '>'
    assert rendered[1][5] == '^'
    assert rendered[3][5] == 'v'


def test_single_top_opening():
    cell = Cell(
        left=False,
        right=False,
        front=False,
        back=False,
        top=True,
        bottom=False,
    )
    rendered =  render_cell(cell)
    assert rendered[2][5] == 'U'
    # sanity check
    assert rendered[2][4] == ' '
    assert rendered[2][6] == ' '


def test_single_bottom_opening():
    cell = Cell(
        left=False,
        right=False,
        front=False,
        back=False,
        top=False,
        bottom=True,
    )
    rendered =  render_cell(cell)
    assert rendered[2][5] == 'D'
    # sanity check
    assert rendered[2][4] == ' '
    assert rendered[2][6] == ' '


def test_both_top_and_bottom_open():
    cell = Cell(
        left=False,
        right=False,
        front=False,
        back=False,
        top=True,
        bottom=True,
    )
    rendered =  render_cell(cell)
    assert rendered[2][5] == ' '
    assert rendered[2][4] == 'U'
    assert rendered[2][6] == 'D'
