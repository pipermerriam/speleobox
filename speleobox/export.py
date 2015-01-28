import os

from speleobox.datastructures import (
    PanelCoordinate,
)
from speleobox.generate import (
    apply_path_to_box,
    generate_path,
)
from speleobox.learning.search import (
    get_learning_tracker,
    get_learning_move_choices,
)
from speleobox.rendering import (
    render_box,
)
from speleobox.utils import (
    generate_empty_box,
)


def path_to_file_path(path):
    filename = 'examples/{0}.txt'.format(''.join((w[0] for w in path)))
    return filename

def find_paths():
    entrance = PanelCoordinate(1, 3, 1, 'back')
    _exit = PanelCoordinate(1, 0, 1, 'front')

    while True:
        path = generate_path(
            entrance, _exit, generate_empty_box(4, 4, 4),
            tracker_getter=get_learning_tracker,
            get_choices_callback=get_learning_move_choices,
        )
        filename = path_to_file_path(path)
        if os.path.exists(filename):
            continue
        print "writing: {0}".format(filename)
        box = apply_path_to_box(entrance, path, generate_empty_box(4, 4, 4))
        export_box(filename, box)


def export_box(path, box):
    with open(path, 'w') as file:
        file.writelines((''.join(line) + '\n' for line in render_box(box)))
