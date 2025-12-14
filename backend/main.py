from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    email: str
    password: str

@app.post("/signup")
def signup(user: User):
    return {"message": "Signup successful"}

@app.post("/login")
def login(user: User):
    return {"message": "Login successful"}
