from . import otherRouter

import random

@otherRouter.get("/remove/")
def add():

    return {"message":"remove"}

@otherRouter.get("/test/")
def test(): 
    return "test"

@otherRouter.get("/other/{other}")
async def otherAPI(other):
    """
    接收任意参数
    """

    return {
        "message": other
    }


@otherRouter.get("/random")
def random(start: int = 0, end: int = 1000, base: int | None = None):

    return {
        "message": random.randint(start,end)
    }