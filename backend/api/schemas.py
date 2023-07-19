from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str 
    email: str 
    icon_image: str 
    introduction: str 
    oshimen: str


class Event(BaseModel):
    id: str
    date: str 
    venue: str 
    target: str 
    type: str


class Report(BaseModel):
    id: str
    author: User
    event: Event
    feedback: str 
    description: str 
    created_at: str


class CreateReport(BaseModel):
    event: Event