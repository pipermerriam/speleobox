import collections


LEFT = 'left'
RIGHT = 'right'
TOP = 'top'
BOTTOM = 'bottom'
FRONT = 'front'
BACK = 'back'

DIRECTIONS = (
    LEFT,
    RIGHT,
    TOP,
    BOTTOM,
    FRONT,
    BACK,
)


IN = 'in'
OUT = 'out'


"""
(-)  front
     -----
left |   | right
     -----
     back  (+)
"""
Cell = collections.namedtuple(
    'Cell',
    (LEFT, RIGHT, TOP, BOTTOM, FRONT, BACK),
)


CellCoordinate = collections.namedtuple(
    'Coordinate',
    ('level', 'y', 'x'),
)

PanelCoordinate = collections.namedtuple(
    'Coordinate',
    ('level', 'y', 'x', 'panel'),
)
