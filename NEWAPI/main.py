from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=[ "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*'],
)


todos = []
class Course(BaseModel):
    id: int
    todo: str

@app.get("/todo", tags=['todos'])

async def root()->dict:

    return {"data" : todos}




@app.post("/todo", tags=["todos"])

def add_todo(todo:Course) -> dict:

    todos.append(todo.dict())

    return todos[-1]