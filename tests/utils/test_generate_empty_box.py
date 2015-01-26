from speleobox.utils import generate_empty_box


def test_generation():
    box = generate_empty_box(2, 3, 4)
    assert len(box) == 2
    assert all(len(layer) == 3 for layer in box)
    assert all(
        all(len(row) == 4 for row in layer) for layer in box
    )
    assert all(
        all(all(not any(cell) for cell in row) for row in layer) for layer in box
    )
