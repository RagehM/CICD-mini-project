from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class StudentBase(BaseModel):
    """Base schema with shared fields for Student models."""
    name: str = Field(..., description="The student's full name")
    university: str = Field(..., description="The university the student attends")
    age: int = Field(..., ge=0, lt=150, description="The student's age")

class StudentCreate(StudentBase):
    """Schema for creating a new student."""
    pass

class Student(StudentBase):
    """Schema for returning a student with database fields."""
    id: int = Field(..., description="The unique identifier for the student")
    
    # Use ConfigDict instead of Config class
    model_config = ConfigDict(from_attributes=True)  # formerly orm_mode
