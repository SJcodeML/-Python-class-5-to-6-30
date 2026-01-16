
from fastapi import FastAPI


app = FastAPI()


def greet():
    return {"message": "Hello, World!"}