import pytest

from speleobox.datastructures import (
    PanelCoordinate,
    LEFT,
    BACK,
)
from speleobox.learning.models import Node
from speleobox.learning.search import (
    FailedChoices,
)


@pytest.mark.django_db
def test_adding_root_path_creates_node():
    entrance = PanelCoordinate(0, 0, 0, LEFT)
    _exit = PanelCoordinate(0, 1, 0, LEFT)
    dimensions = (1, 2, 2)
    tracker = FailedChoices(entrance, _exit, dimensions)

    path = [BACK]

    assert not Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="b",
    ).exists()

    tracker.add(path)

    assert Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="b",
    ).exists()


@pytest.mark.django_db
def test_adding_child_creates_parent_chain():
    entrance = PanelCoordinate(0, 0, 0, LEFT)
    _exit = PanelCoordinate(0, 1, 0, LEFT)
    dimensions = (1, 2, 2)
    tracker = FailedChoices(entrance, _exit, dimensions)

    path = [BACK, LEFT, BACK]

    assert not Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="blb",
    ).exists()
    assert not Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="bl",
    ).exists()
    assert not Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="b",
    ).exists()

    tracker.add(path)

    assert Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="blb",
    ).exists()
    assert Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="bl",
    ).exists()
    assert Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="b",
    ).exists()


@pytest.mark.django_db
def test_adding_child_with_some_existing_and_some_missing():
    entrance = PanelCoordinate(0, 0, 0, LEFT)
    _exit = PanelCoordinate(0, 1, 0, LEFT)
    dimensions = (1, 2, 2)
    tracker = FailedChoices(entrance, _exit, dimensions)

    path = [BACK, LEFT, BACK, LEFT]

    root = Node.add_root(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="b",
    )
    root.add_child(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="bl",
    )
    assert not Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="blb",
    ).exists()
    assert not Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="blbl",
    ).exists()

    tracker.add(path)

    assert Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="blb",
    ).exists()
    assert Node.objects.filter(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="blbl",
    ).exists()


@pytest.mark.django_db
def test_contains_with_existing_node():
    entrance = PanelCoordinate(0, 0, 0, LEFT)
    _exit = PanelCoordinate(0, 1, 0, LEFT)
    dimensions = (1, 2, 2)
    tracker = FailedChoices(entrance, _exit, dimensions)

    path = [BACK, LEFT, BACK, LEFT]

    Node.add_root(
        entrance="0:0:0:left",
        exit="0:1:0:left",
        dimensions="1:2:2",
        value="blbl",
    )

    assert path in tracker


@pytest.mark.django_db
def test_contains_with_missing_node():
    entrance = PanelCoordinate(0, 0, 0, LEFT)
    _exit = PanelCoordinate(0, 1, 0, LEFT)
    dimensions = (1, 2, 2)
    tracker = FailedChoices(entrance, _exit, dimensions)

    path = [BACK, LEFT, BACK, LEFT]

    assert path not in tracker
