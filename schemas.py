from typing import List, Optional
from pydantic import BaseModel,conlist

from datetime import datetime



class Song(BaseModel):
    id:int
    name:str
    duration:int
    upload_time:Optional[datetime]

    class Config:
        orm_mode = True


class Podcast(BaseModel):
    id:int
    name:str
    duration:int
    upload_time:Optional[datetime]
    host:str
    participants:conlist(str,max_items=100)

    class Config:
        orm_mode=True


class Audiobook(BaseModel):
    id:int
    title:str
    author:str
    narrator:str
    duration:int
    upload_time:Optional[datetime]

    class Config:
        orm_mode = True

