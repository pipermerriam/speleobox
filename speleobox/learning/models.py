from django.db import models

from treebeard.mp_tree import MP_Node


class Node(MP_Node):
    value = models.CharField(max_length=255)
    entrance = models.CharField(max_length=15)
    exit = models.CharField(max_length=15)

    steplen = 1
