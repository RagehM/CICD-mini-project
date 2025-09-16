from pydantic import BaseModel

# Base schema (shared fields)
class StudentBase(BaseModel):
    name: str
    university: str
    age: int

# Schema for creating a student (request body)
class StudentCreate(StudentBase):
    pass

# Schema for returning a student (response)
class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
