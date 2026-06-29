from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Rahul'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0.0, lt=10, default=5)

new_student = {'age': '32', 'email': 'abc@abc.com', 'cgpa': 12}

student = Student(**new_student)

print(student)