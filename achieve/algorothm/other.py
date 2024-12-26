from typing import List


def merger_two_sort_arr(arr1: List[int], arr2: List[int]):
    """
    合并两个有序数组
    Args:
        arr1:
        arr2:

    Returns:

    """

    i = 0
    j = 0
    t = min(len(arr1), len(arr2))
    result = []
    while i < t and j < t:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result += arr1[i:]
    result += arr2[j:]

    return result


