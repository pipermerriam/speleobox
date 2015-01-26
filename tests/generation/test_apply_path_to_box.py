from speleobox.datastructures import (
    IN,
    OUT,
    LEFT,
    RIGHT,
    BACK,
    PanelCoordinate,
)
from speleobox.generate import (
    apply_path_to_box,
)
from speleobox.utils import (
    generate_empty_box,
)


def test_apply_path_to_box():
    path = (RIGHT, BACK, LEFT, LEFT)


    box = apply_path_to_box(
        entrance=PanelCoordinate(0, 0, 0, LEFT),
        path=path,
        box=generate_empty_box(1, 2, 2),
    )

    front_left, front_right = box[0][0]
    back_left, back_right = box[0][1]

    assert front_left.left == IN
    assert front_left.right == OUT

    assert front_right.left == IN
    assert front_right.back == OUT

    assert back_right.front == IN
    assert back_right.left == OUT

    assert back_left.right == IN
    assert back_left.left == OUT
