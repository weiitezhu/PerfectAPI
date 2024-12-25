from fastapi import APIRouter
from .sorting import sortRouter

algorithmRouter = APIRouter()
algorithmRouter.include_router(sortRouter, prefix="", tags = ["sortRouter"])
