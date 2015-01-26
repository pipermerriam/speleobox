from speleobox.datastructures import (
    LEFT,
    RIGHT,
    BACK,
    PanelCoordinate,
)
from speleobox.generate import (
    generate_path,
)
from speleobox.utils import (
    generate_empty_box,
)


def test_small_two_by_two_box():
    box = generate_empty_box(1, 2, 2)
    entrance = PanelCoordinate(0, 0, 0, LEFT)
    _exit = PanelCoordinate(0, 1, 0, LEFT)

    path = generate_path(
        entrance=entrance,
        _exit=_exit,
        box=box,
    )
    assert path == (RIGHT, BACK, LEFT, LEFT)


def test_three_by_three_box():
    solutions = (
        ('right', 'right', 'back', 'left', 'left', 'back', 'right', 'right', 'right'),
        ('back', 'back', 'right', 'front', 'front', 'right', 'back', 'back', 'right'),
    )
    box = generate_empty_box(1, 3, 3)
    entrance = PanelCoordinate(0, 0, 0, LEFT)
    _exit = PanelCoordinate(0, 2, 2, RIGHT)

    path = generate_path(
        entrance=entrance,
        _exit=_exit,
        box=box,
    )
    assert path in solutions
