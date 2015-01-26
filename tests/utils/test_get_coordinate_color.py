import pytest

from speleobox.datastructures import CellCoordinate
from speleobox.utils import (
    WHITE,
    BLACK,
    generate_empty_box,
    get_coordinate_color,
)


@pytest.mark.parametrize(
    'coordinate,expected',
    (
        (CellCoordinate(0, 0, 0), WHITE),
        (CellCoordinate(1, 1, 0), WHITE),
        (CellCoordinate(0, 1, 1), WHITE),
        (CellCoordinate(1, 0, 1), WHITE),
        (CellCoordinate(1, 1, 1), BLACK),
        (CellCoordinate(0, 1, 0), BLACK),
        (CellCoordinate(0, 0, 1), BLACK),
        (CellCoordinate(1, 0, 0), BLACK),
        (CellCoordinate(2, 2, 2), WHITE),
        (CellCoordinate(2, 3, 2), BLACK),
    )
)
def test_get_coordinate_color(coordinate, expected):
    actual = get_coordinate_color(coordinate)
    assert actual == expected
