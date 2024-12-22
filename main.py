from fastapi import FastAPI
from apps.math import mathRouter
from apps.other import otherRouter

app = FastAPI()


app.include_router(mathRouter, prefix="", tags = ["math"])
app.include_router(otherRouter, prefix="", tags = ["other"])


@app.get(f"/")
def read_root():    
    return {"message": "Hello World"}

