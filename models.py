from pydantic import BaseModel
from typing import List

class Organization(BaseModel):
    id: int
    name: str
    phones: List[str]
    building_id: int
    functionals: List[int]

class Building(BaseModel):
    address: str
    sh: float
    dol: float

class Functional(BaseModel):
    id: int
    fun_id: List[str]

class Building(BaseModel):
    address: str
    sh: float
    dol: float

class Functional(BaseModel):
    id: int
    fun_id: List[str]

class Organization(BaseModel):
    id: int
    name: str
    phones: List[str]
    building: Building
    functionals: List[Functional]