import pytest

from speleobox.datastructures import (
    LEFT,
    RIGHT,
    TOP,
    BOTTOM,
    FRONT,
    BACK,
    Cell,
    PanelCoordinate,
)
from speleobox.utils import (
    generate_empty_box,
    is_edge,
)

def test_bad_coordinate():
    box = generate_empty_box(1, 2, 2)
    coordinate = PanelCoordinate(
        level=0, y=2, x=1, panel=TOP,
    )
    with pytest.raises(IndexError):
        is_edge(coordinate, box)


def test_with_non_edges():
    box = generate_empty_box(1, 2, 2)

    #  ------
    #  | || |
    #  -x----
    #  ------
    #  | || |
    #  ------
    assert not is_edge(PanelCoordinate(
        level=0, y=0, x=0, panel=BACK,
    ), box)

    #  ------
    #  | x| |
    #  ------
    #  ------
    #  | || |
    #  ------
    assert not is_edge(PanelCoordinate(
        level=0, y=0, x=0, panel=RIGHT,
    ), box)

    #  ------
    #  | |x |
    #  ------
    #  ------
    #  | || |
    #  ------
    assert not is_edge(PanelCoordinate(
        level=0, y=0, x=1, panel=LEFT,
    ), box)

    #  ------
    #  | || |
    #  ----x-
    #  ------
    #  | || |
    #  ------
    assert not is_edge(PanelCoordinate(
        level=0, y=0, x=1, panel=BACK,
    ), box)

    #  ------
    #  | || |
    #  ------
    #  -x----
    #  | || |
    #  ------
    assert not is_edge(PanelCoordinate(
        level=0, y=1, x=0, panel=FRONT,
    ), box)

    #  ------
    #  | || |
    #  ------
    #  ------
    #  | x| |
    #  ------
    assert not is_edge(PanelCoordinate(
        level=0, y=1, x=0, panel=RIGHT,
    ), box)

    #  ------
    #  | || |
    #  ------
    #  ------
    #  | |x |
    #  ------
    assert not is_edge(PanelCoordinate(
        level=0, y=1, x=1, panel=LEFT,
    ), box)

    #  ------
    #  | || |
    #  ------
    #  ----x-
    #  | || |
    #  ------
    assert not is_edge(PanelCoordinate(
        level=0, y=1, x=1, panel=FRONT,
    ), box)


def test_with_edges():
    box = generate_empty_box(1, 2, 2)

    #  -x----
    #  | || |
    #  ------
    #  ------
    #  | || |
    #  ------
    assert is_edge(PanelCoordinate(
        level=0, y=0, x=0, panel=FRONT,
    ), box)

    #  ------
    #  x || |
    #  ------
    #  ------
    #  | || |
    #  ------
    assert is_edge(PanelCoordinate(
        level=0, y=0, x=0, panel=LEFT,
    ), box)

    # TOP and BOTTOM
    assert is_edge(PanelCoordinate(
        level=0, y=0, x=0, panel=TOP,
    ), box)
    assert is_edge(PanelCoordinate(
        level=0, y=0, x=0, panel=BOTTOM,
    ), box)

    #  ------
    #  | || x
    #  ------
    #  ------
    #  | || |
    #  ------
    assert is_edge(PanelCoordinate(
        level=0, y=0, x=1, panel=RIGHT,
    ), box)

    #  ----x-
    #  | || |
    #  ------
    #  ------
    #  | || |
    #  ------
    assert is_edge(PanelCoordinate(
        level=0, y=0, x=1, panel=FRONT,
    ), box)

    # TOP and BOTTOM
    assert is_edge(PanelCoordinate(
        level=0, y=0, x=1, panel=TOP,
    ), box)
    assert is_edge(PanelCoordinate(
        level=0, y=0, x=1, panel=BOTTOM,
    ), box)


    #  ------
    #  | || |
    #  ------
    #  ------
    #  | || |
    #  -x----
    assert is_edge(PanelCoordinate(
        level=0, y=1, x=0, panel=BACK,
    ), box)

    #  ------
    #  | || |
    #  ------
    #  ------
    #  x || |
    #  ------
    assert is_edge(PanelCoordinate(
        level=0, y=1, x=0, panel=LEFT,
    ), box)

    # TOP and BOTTOM
    assert is_edge(PanelCoordinate(
        level=0, y=1, x=0, panel=TOP,
    ), box)
    assert is_edge(PanelCoordinate(
        level=0, y=1, x=0, panel=BOTTOM,
    ), box)

    #  ------
    #  | || |
    #  ------
    #  ------
    #  | || x
    #  ------
    assert is_edge(PanelCoordinate(
        level=0, y=1, x=1, panel=RIGHT,
    ), box)

    #  ------
    #  | || |
    #  ------
    #  ------
    #  | || |
    #  ----x-
    assert is_edge(PanelCoordinate(
        level=0, y=1, x=1, panel=BACK,
    ), box)

    # TOP and BOTTOM
    assert is_edge(PanelCoordinate(
        level=0, y=1, x=1, panel=TOP,
    ), box)
    assert is_edge(PanelCoordinate(
        level=0, y=1, x=1, panel=BOTTOM,
    ), box)
