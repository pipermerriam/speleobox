import collections

from speleobox.learning.search import (
    weighted_random,
)


def test_weighted_random():
    weights = {'a': 1, 'b': 9}
    counter = collections.Counter()

    for i in range(10000):
        counter[weighted_random(weights)] += 1

    a_counts = counter['a']
    b_counts = counter['b']

    assert abs(a_counts - 1000) < 200
    assert abs(b_counts - 9000) < 800
