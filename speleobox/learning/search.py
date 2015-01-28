import random

from speleobox.utils import (
    get_box_dimensions,
)
from speleobox.generate import (
    get_valid_moves,
    apply_path_to_box,
)

from speleobox.learning.models import Node


def weighted_random(pairs):
    total = sum(pair[1] for pair in pairs.items())
    r = random.randint(1, total)
    for (value, weight) in sorted(pairs.items(), key=lambda v: v[1]):
        r -= weight
        if r <= 0:
            return value


def get_learning_move_choices(coordinate, entrance, _exit, path, box, failed_paths):
    move_choices = get_valid_moves(
        coordinate,
        apply_path_to_box(entrance, path, box),
    )
    weights = {}
    entrance_string = "{level}:{y}:{x}:{panel}".format(
        level=entrance.level,
        y=entrance.y,
        x=entrance.x,
        panel=entrance.panel,
    )
    exit_string = "{level}:{y}:{x}:{panel}".format(
        level=_exit.level,
        y=_exit.y,
        x=_exit.x,
        panel=_exit.panel,
    )

    dimensions = get_box_dimensions(box)
    dimensions_string = "{levels}:{depth}:{width}".format(
        levels=dimensions[0],
        depth=dimensions[1],
        width=dimensions[2],
    )
    for direction in move_choices.keys():
        if tuple(path + [direction]) in failed_paths:
            continue
        direction_path_string = ''.join([v[0] for v in tuple(path + [direction])])
        try:
            node = Node.objects.get(
                entrance=entrance_string,
                exit=exit_string,
                dimensions=dimensions_string,
                value=direction_path_string,
            )
        except Node.DoesNotExist:
            weights[direction] = 1
        else:
            weights[direction] = node.get_descendants().filter(is_dead_end=True).count() or 1

    choices = []
    while weights:
        choice = weighted_random(weights)
        weights.pop(choice)
        choices.append(choice)

    return tuple(reversed(choices))


class FailedChoices(object):
    def __init__(self, entrance, _exit, dimensions):
        self.entrance_string = "{level}:{y}:{x}:{panel}".format(
            level=entrance.level,
            y=entrance.y,
            x=entrance.x,
            panel=entrance.panel,
        )
        self.exit_string = "{level}:{y}:{x}:{panel}".format(
            level=_exit.level,
            y=_exit.y,
            x=_exit.x,
            panel=_exit.panel,
        )
        self.dimensions_string = "{levels}:{depth}:{width}".format(
            levels=dimensions[0],
            depth=dimensions[1],
            width=dimensions[2],
        )
        self.seen_paths = set()

    def __len__(self):
        return 1

    def __contains__(self, item):
        if item in self.seen_paths:
            return True
        path_string = ''.join([v[0] for v in item])
        try:
            node = Node.objects.get(
                entrance=self.entrance_string,
                exit=self.exit_string,
                dimensions=self.dimensions_string,
                value=path_string,
            )
        except Node.DoesNotExist:
            return False
        else:
            return node.is_leaf()

    def add(self, path):
        node = self._add(path)
        if node.is_dead_end != node.is_leaf():
            node.is_dead_end = node.is_leaf()
            node.save()
        return node

    def _add(self, path):
        self.seen_paths.add(path)
        path_string = ''.join([v[0] for v in path])
        create_kwargs = {
            'entrance': self.entrance_string,
            'exit': self.exit_string,
            'dimensions': self.dimensions_string,
            'value': path_string,
        }
        try:
            node = Node.objects.get(**create_kwargs)
        except Node.DoesNotExist:
            if len(path_string) == 0:
                return
            elif len(path_string) == 1:
                node = Node.add_root(**create_kwargs)
            else:
                parent = self._add(path[:-1])
                node = parent.add_child(**create_kwargs)
        return node


def get_learning_tracker(entrance, _exit, dimensions):
    return FailedChoices(entrance, _exit, dimensions)
