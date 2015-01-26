from speleobox.utils import (
    get_cell_count,
    generate_empty_box,
)


def test_cell_counts():
    assert get_cell_count(generate_empty_box(4, 4, 4)) == 64
    assert get_cell_count(generate_empty_box(1, 3, 3)) == 9
    assert get_cell_count(generate_empty_box(1, 1, 1)) == 1
