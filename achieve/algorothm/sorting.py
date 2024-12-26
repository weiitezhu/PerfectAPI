from typing import List
from other import merger_two_sort_arr


def bubble_sort(arr: List[int]):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insert_sort(arr: List[int]):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def quick_sort(arr: List[int], i=None, j=None):
    """
    快速排序
    Args:
        arr:

    Returns:

    """


def merger_sort(arr: List[int]):
    """
    归并排序
    Args:
        arr:

    Returns:

    """
    if len(arr) == 1:
        return arr

    m = len(arr) // 2

    left = merger_sort(arr[:m])
    right = merger_sort(arr[m:])

    return merger_two_sort_arr(left, right)
