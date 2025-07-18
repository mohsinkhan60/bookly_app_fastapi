from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/greet")
async def read_item(name: Optional[str] = "User", age: int = 0):
      return {f"Hellow {name}" f" and Your age is {age}"}

@app.post("/create_book/")
async def create_book():
     pass