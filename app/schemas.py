from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentCreate(BaseModel):
    title: str
    content: str

class DocumentOut(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    question: str

class QuestionOut(BaseModel):
    id: int
    question: str
    answer: Optional[str]
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
