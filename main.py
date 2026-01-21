from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message":"Hello world"}

@app.get("/greet")
async def greet_namefn(name:str = "user",age:int=0) -> dict:
    return {"message":f"Hello, {name}!", "age": age }