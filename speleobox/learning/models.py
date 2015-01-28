from django.db import models

from treebeard.mp_tree import MP_Node


class Node(MP_Node):
    value = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=15)
    entrance = models.CharField(max_length=15)
    exit = models.CharField(max_length=15)
    is_dead_end = models.BooleanField(default=False)

    steplen = 1

    class Meta:
        index_together = (
            ("value", "entrance", "exit", "dimensions", "is_dead_end"),
        )
