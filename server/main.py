
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI Mini-Lab!"}


import requests

@app.get("/users")
def get_users():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=10
    )
    return response.json()
