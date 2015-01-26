from speleobox.datastructures import (
    LEFT,
    RIGHT,
    TOP,
    BOTTOM,
    FRONT,
    BACK,
    DIRECTIONS,
    Cell,
    CellCoordinate,
)


def generate_empty_box(levels, depth, width):
    return tuple((
        tuple((
            tuple((
                Cell(*((False,) * 6)) for _ in range(width)
            ))  for _ in range(depth)
        )) for _ in range(levels)
    ))


def get_cell(coordinate, box):
    level = coordinate.level
    y = coordinate.y
    x = coordinate.x

    if level < 0 or y < 0 or x < 0:
        raise IndexError("Coordinate (level, y, x) does not exist")

    try:
        return box[level][y][x]
    except IndexError:
        raise IndexError("Coordinate (level, y, x) does not exist")


def set_cell(coordinate, cell, box):
    level = coordinate.level
    y = coordinate.y
    x = coordinate.x

    if level < 0 or y < 0 or x < 0:
        raise IndexError("Coordinate (level, y, x) does not exist")

    box[level][y][x] = cell


MOVES = {
    LEFT: (0, 0, -1),
    RIGHT: (0, 0, 1),
    TOP: (1, 0, 0),
    BOTTOM: (-1, 0, 0),
    FRONT: (0, -1, 0),
    BACK: (0, 1, 0),
}


REVERSE_MOVES = {
    LEFT: RIGHT,
    RIGHT: LEFT,
    TOP: BOTTOM,
    BOTTOM: TOP,
    FRONT: BACK,
    BACK: FRONT,
}

def move(coordinate, direction):
    level, y, x = map(sum, zip(
        (coordinate.level, coordinate.y, coordinate.x),
        MOVES[direction],
    ))
    return CellCoordinate(level=level, y=y, x=x)


def is_edge(coordinate, box):
    # make sure the coordinate exists
    get_cell(coordinate, box)

    neighbor_coordinate = move(coordinate, coordinate.panel)

    if any(v < 0 for v in neighbor_coordinate):
        return True

    try:
        get_cell(neighbor_coordinate, box)
    except IndexError:
        return True
    else:
        return False


def _get_neighbor_coordinates(coordinate):
    for direction in DIRECTIONS:
        yield move(coordinate, direction)


def get_neighbor_coordinates(*args, **kwargs):
    return tuple(_get_neighbor_coordinates(*args, **kwargs))


def _get_neighbors(coordinate, box):
    for neighbor_coord in get_neighbor_coordinates(coordinate):
        try:
            yield get_cell(neighbor_coord, box)
        except IndexError:
            yield None


def get_neighbors(*args, **kwargs):
    return tuple(_get_neighbors(*args, **kwargs))


WHITE = 'white'
BLACK = 'black'


def get_coordinate_color(coordinate):
    """
    If you colored the box with a checker pattern of black and white boxes with
    (0, 0, 0) being white, what color would the coordinate be.
    """
    if (coordinate.y + coordinate.x) % 2:
        is_white = False
    else:
        is_white = True

    if coordinate.level % 2:
        is_white = not is_white

    if is_white:
        return WHITE
    else:
        return BLACK


def get_cell_count(box):
    return sum(
        sum(len(row) for row in layer) for layer in box
    )


def mutable_copy(box):
    return list((
        list((
            list((cell for cell in row)) for row in level
        )) for level in box
    ))


def immutable_copy(box):
    return tuple((
        tuple((
            tuple((cell for cell in row)) for row in level
        )) for level in box
    ))


def enumerate_box_coordinates(box):
    for level, x in enumerate(box):
        for row, y in enumerate(x):
            for cell, _ in enumerate(y):
                yield CellCoordinate(level=level, y=row, x=cell)
