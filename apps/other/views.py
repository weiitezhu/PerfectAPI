from typing import Optional,List, Any
from fastapi import Query, Path
import random


from . import otherRouter
from .structs import Item

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


@otherRouter.get("/random/")
def randomnum(start: int = 0, end: int = 1000, base: Optional[int]= None):

    return {
        "message": random.randint(start,end)
    }

@otherRouter.post("/item/")
def item(item:Item):
    # 提交一点信息
    return item



@otherRouter.get("/Verify phone number")
def verify_phone_number(number: str = Query(length=11)):
   # 验证手机号
    return {
        "message": "success",
        "number":number
    }

@otherRouter.get("/Verify phone number/{number}/")
def verify_phone_number(number: str = Path(length=11)):
    # 验证手机号
    return {
        "message": "success",
        "number":number
    }

@otherRouter.get("/Verify phone numbers")
def verify_phone_number(numbers: List[str] = Query(length=11)):
    # 验证多个手机号？
    return {
        "message": "success",
        "number":numbers
    }


@otherRouter.get("/Verify email")
def verify_email(email: str = Query(pattern="^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$")):
    # 验证邮箱是否合法
    return {
        "message": "success",
        "email":email
    }

#========================================examples===========================================

from fastapi import Body
from pydantic import BaseModel, HttpUrl
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID
class Image(BaseModel):
    url: HttpUrl
    name: str


class Option(BaseModel):
    name: str
    desc: str | None
    pk: int
    tags: set[str] = set()
    image: Image | None = None


class OptionData(BaseModel):
    name: str
    desc: str | None
    pk: int
    options: List[Option] = []

class User(BaseModel):
    username: str
    full_name: str | None = None

@otherRouter.put("/examples/{path_data_one}/{path_data_two}")
async def __examples(
                path_data_one: str| int | None,  # 路径参数
                path_data_two, 
                user: Annotated[User, Body()],  # 请求体参数
                options: OptionData, 
                q: str # 查询参数
                ):
    pass

# from doc
@otherRouter.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }


class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: str | None = None


@otherRouter.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user