from apis.algorithm import algorithmRouter
from typing import List
from fastapi import Query, Path

from achieve.algorothm.sorting import bubble_sort


@algorithmRouter.get("/algorithmRouter/bubble sort")
async def bubble_sort_api(arr: List[int] = Query()):
    bubble_sort(arr)
    return {
        "message": "success",
        "result": arr
    }
