from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

fackdb =[]

class Course(BaseModel):
    id: int
    name: str
    price: float
    is_early_bird: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/courses")
def get_courses():
    return fackdb


@app.get("/courses/{course_id}")
def get_a_courses(course_id: int):
    course  = course_id -1
    return fackdb[course]

@app.post("/courses")
def add_course(course: Course):
    fackdb.append(course.dict())
    return fackdb[-1]

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    fackdb.pop(course_id-1)
    return {"task": "deletion"}