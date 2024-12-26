import random


def test_merger_sort_arr():
    from achieve.algorothm.other import merger_two_sort_arr
    a = [i for i in range(10)]
    b = [i for i in range(10)]
    ret = merger_two_sort_arr(a, b)
    assert sum(ret) == sum(a) * 2
