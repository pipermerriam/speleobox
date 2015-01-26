import pytest

from speleobox.datastructures import CellCoordinate
from speleobox.utils import (
    generate_empty_box,
    get_neighbors,
)


def test_get_neighbors():
    box = generate_empty_box(2, 2, 2)

    left, right, top, bottom, front, back = get_neighbors(
        CellCoordinate(level=0, y=0, x=0), box,
    )
    assert not left
    assert right
    assert top
    assert not bottom
    assert not front
    assert back
