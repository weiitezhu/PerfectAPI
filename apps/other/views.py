from typing import Optional,List
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
def random(start: int = 0, end: int = 1000, base: Optional[int]= None):

    return {
        "message": random.randint(start,end)
    }

@otherRouter.post("/item/")
def item(item:Item):
    
    return item



@otherRouter.get("/Verify phone number")
def verify_phone_number(number: str = Query(length=11)):

    return {
        "message": "success",
        "number":number
    }

@otherRouter.get("/Verify phone number/{number}/")
def verify_phone_number(number: str = Path(length=11)):

    return {
        "message": "success",
        "number":number
    }

@otherRouter.get("/Verify phone numbers")
def verify_phone_number(numbers: List[str] = Query(length=11)):

    return {
        "message": "success",
        "number":numbers
    }


@otherRouter.get("/Verify email")
def verify_email(email: str = Query(pattern="^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$")):

    return {
        "message": "success",
        "email":email
    }