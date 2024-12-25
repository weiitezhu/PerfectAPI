from . import sortRouter
from typing import List
from fastapi import Query, Path



@sortRouter.get("/bubble sort")
async def bubble_sort(arr: List[int]=Query()):

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr [j+ 1]:
                arr[j], arr[j+1] = arr[j+ 1], arr[j]
    

    return {
        "message": "success",
        "result": arr
    }
