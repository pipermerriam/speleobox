import pytest

from speleobox.datastructures import (
    LEFT,
    RIGHT,
    PanelCoordinate,
)
from speleobox.utils import (
    get_cell,
    get_coordinate_color,
    generate_empty_box,
)
from speleobox.generate import (
    generate_path,
    INVALID_ENTRANCE,
    INVALID_EXIT,
    IMPOSSIBLE_TO_FILL_SPACE,
)


def test_bad_entrance():
    box = generate_empty_box(2, 2, 2)
    entrance = PanelCoordinate(level=1, y=1, x=1, panel=LEFT)
    exit = PanelCoordinate(level=0, y=0, x=0, panel=LEFT)

    with pytest.raises(ValueError) as err:
        generate_path(entrance, exit, box)

    assert err.value.message == INVALID_ENTRANCE


def test_bad_exit():
    box = generate_empty_box(2, 2, 2)
    entrance = PanelCoordinate(level=0, y=0, x=0, panel=LEFT)
    exit = PanelCoordinate(level=1, y=1, x=1, panel=LEFT)

    with pytest.raises(ValueError) as err:
        generate_path(entrance, exit, box)

    assert err.value.message == INVALID_EXIT


def test_good_entrance_and_exit():
    box = generate_empty_box(2, 2, 2)
    entrance = PanelCoordinate(level=0, y=0, x=0, panel=LEFT)
    exit = PanelCoordinate(level=1, y=1, x=1, panel=RIGHT)

    generate_path(entrance, exit, box)


def test_impossible_entrance_exit_combo_for_even_box():
    box = generate_empty_box(2, 2, 2)
    entrance = PanelCoordinate(level=0, y=0, x=0, panel=LEFT)
    exit = PanelCoordinate(level=0, y=1, x=1, panel=RIGHT)

    # sainity check
    assert get_coordinate_color(entrance) == get_coordinate_color(exit)

    with pytest.raises(ValueError) as err:
        generate_path(entrance, exit, box)

    assert err.value.message == IMPOSSIBLE_TO_FILL_SPACE


def test_impossible_entrance_exit_combo_for_odd_box():
    box = generate_empty_box(3, 3, 3)
    entrance = PanelCoordinate(level=0, y=0, x=0, panel=LEFT)
    exit = PanelCoordinate(level=0, y=1, x=0, panel=LEFT)

    # sainity check
    assert get_coordinate_color(entrance) != get_coordinate_color(exit)

    with pytest.raises(ValueError) as err:
        generate_path(entrance, exit, box)

    assert err.value.message == IMPOSSIBLE_TO_FILL_SPACE
