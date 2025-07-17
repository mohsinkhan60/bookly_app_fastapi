from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/name/{name}")
async def read_item(name: str):
      return {f"Hellow {name}"}