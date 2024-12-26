from typing import List, Any

from fastapi import Query

from . import mathRouter


@mathRouter.get("/math/{other}")
async def other(other: Any):
    """
    接收任意参数
    """

    return {
        "message": other
    }


@mathRouter.get("/add/")
def add(qs: List[int] = Query()):
    return {
        "message": "success",
        "result": sum(qs)
    }
