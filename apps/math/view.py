from . import mathRouter



@mathRouter.get("/math/{other}")
async def other(other):
    """
    接收任意参数
    """

    return {
        "message": other
    }

@mathRouter.get("/add/")
def add():

    return {"message":"xxxx"}