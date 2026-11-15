import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "hello", "env": os.environ.get("APP_ENV", "not set")}