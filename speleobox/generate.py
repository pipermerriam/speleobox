import random

from speleobox.datastructures import (
    IN,
    OUT,
    DIRECTIONS,
    CellCoordinate,
    PanelCoordinate,
)
from speleobox.utils import (
    is_edge,
    move,
    get_cell,
    get_cell_count,
    get_coordinate_color,
    get_neighbor_coordinates,
    get_neighbors,
    REVERSE_MOVES,
    mutable_copy,
    immutable_copy,
    set_cell,
    enumerate_box_coordinates,
    generate_empty_box,
)

INVALID_ENTRANCE = "Entrance coordinate is not on the edge of the box"
INVALID_EXIT = "Exit coordinate is not on the edge of the box"
IMPOSSIBLE_TO_FILL_SPACE = (
    "Not possible to fill the space with the given entrance and exit coordinates"
)


def is_unvisited_cell(cell):
    return sum(map(bool, cell)) == 0


def apply_path_to_box(entrance, path, box):
    box = mutable_copy(box)
    current_coordinate = CellCoordinate(
        level=entrance.level,
        y=entrance.y,
        x=entrance.x,
    )
    entrance_cell = get_cell(entrance, box)
    set_cell(
        entrance,
        entrance_cell._replace(**{entrance.panel: IN}),
        box,
    )

    for direction in path:
        current_cell = get_cell(current_coordinate, box)
        set_cell(
            current_coordinate,
            current_cell._replace(**{direction: OUT}),
            box,
        )

        next_coordinate = move(current_coordinate, direction)

        try:
            next_cell = get_cell(next_coordinate, box)
        except IndexError:
            # We've exited the box which is ok.
            break
        else:
            set_cell(
                next_coordinate,
                next_cell._replace(**{REVERSE_MOVES[direction]: IN}),
                box,
            )
            current_cell = next_cell
            current_coordinate = next_coordinate

    return box


def get_valid_moves(coordinate, box):
    return dict(filter(
        lambda v: v[1] and is_unvisited_cell(v[1]),
        zip(DIRECTIONS, get_neighbors(coordinate, box)),
    ))


def get_marooned_coordinates(current_coordinate, box):
    neighboring_coordinates = get_neighbor_coordinates(
        current_coordinate,
    )
    marooned_coordinates = set()
    for coordinate in enumerate_box_coordinates(box):
        cell = get_cell(coordinate, box)
        if is_unvisited_cell(cell):
            moves = get_valid_moves(coordinate, box)
            if coordinate not in neighboring_coordinates and len(moves) == 1:
                marooned_coordinates.add(coordinate)
        else:
            continue
    return marooned_coordinates


def get_unvisited_coordinates(box):
    unvisited = set()
    for coordinate in enumerate_box_coordinates(box):
        cell = get_cell(coordinate, box)
        if is_unvisited_cell(cell):
            unvisited.add(coordinate)
    return unvisited


def get_path_termination_coordinate(start, path):
    coordinate = CellCoordinate(
        level=start.level,
        y=start.y,
        x=start.x,
    )
    for direction in path:
        coordinate = move(coordinate, direction)
    return coordinate


def generate_path(entrance, _exit, box):
    """
    Given a box, an entrance coordinate, and an exit coordinate generate a path
    to fill the space.
    """
    if not is_edge(entrance, box):
        raise ValueError(INVALID_ENTRANCE)
    if not is_edge(_exit, box):
        raise ValueError(INVALID_EXIT)

    # Check that a space-filling path is possible.
    entrance_color = get_coordinate_color(entrance)
    exit_color = get_coordinate_color(_exit)

    if get_cell_count(box) % 2:
        if entrance_color != exit_color:
            raise ValueError(IMPOSSIBLE_TO_FILL_SPACE)
    else:
        if entrance_color == exit_color:
            raise ValueError(IMPOSSIBLE_TO_FILL_SPACE)

    failed_paths = set()
    path = []

    while len(failed_paths) < 1000000:
        current_coordinate = get_path_termination_coordinate(entrance, path)

        if current_coordinate[:3] == _exit[:3]:
            # We might be at the exit.  Check if the space is filled.  If so,
            # add the exit direction to the path and break out.
            unvisited = get_unvisited_coordinates(
                apply_path_to_box(entrance, path, box),
            )
            if unvisited:
                failed_paths.add(tuple(path))
                path.pop()
                continue
            path.append(_exit.panel)
            break
        move_choices = get_valid_moves(
            current_coordinate,
            apply_path_to_box(entrance, path, box),
        )
        while move_choices:
            direction = random.choice(move_choices.keys())
            move_choices.pop(direction)
            path.append(direction)
            if tuple(path) in failed_paths:
                # We've already tried this choice and it is bad.
                path.pop()
                continue
            marooned_coordinates = get_marooned_coordinates(
                move(current_coordinate, direction),
                apply_path_to_box(entrance, path, box)
            )

            if marooned_coordinates:
                if len(marooned_coordinates) == 1 and tuple(marooned_coordinates)[0][:3] == _exit[:3]:
                    # Edge case is the exit coordinate.
                    break
                else:
                    failed_paths.add(tuple(path))
                    path.pop()
            else:
                # This choice does not maroon any coordinates, so break out of
                # the loop and move to the next cell.
                break
        else:
            # Error:
            # None of the move choices produced a box state that didn't contain
            # any marooned cells.  That means the current path is bad so we
            # step back up and try another choice.
            failed_paths.add(tuple(path))
            path.pop()
    else:
        # Error:
        # Didn't find a path?
        raise ValueError("Could not find a path")

    return tuple(path)


def generate_box(levels, depth, width):
    box = generate_empty_box(levels, depth, width)
    level = 0 if levels == 1 else 1
    entrance_x = 0 if width == 1 else 1
    entrance_y = depth - 1

    entrance = PanelCoordinate(level, entrance_y, entrance_x, 'back')

    entrance_color = get_coordinate_color(entrance)

    for x in range(width, -1, -1):
        coord = PanelCoordinate(level, 0, x, 'front')
        coord_color = get_coordinate_color(coord)
        if get_cell_count(box) % 2 and entrance_color != coord_color:
            continue
        elif not get_cell_count(box) % 2 and entrance_color == coord_color:
            continue
        else:
            _exit = coord
            break
    else:
        raise ValueError("Couldn't find an exit panel")

    path = generate_path(entrance, _exit, box)
    return apply_path_to_box(entrance, path, box)
