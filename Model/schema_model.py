from pydantic import BaseModel
from typing import List

class Column(BaseModel):
    name:str
    type:str

class Schema(BaseModel):
    table:str
    columns:List[Column]