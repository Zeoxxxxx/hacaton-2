from typing import Union
from fastapi import FastAPI
from pydantic.v1 import BaseModel
from starlette.authentication import BaseUser
from enum import Enum
from datetime import date, datetime

app = FastAPI()

class Vkuser(BaseModel): # вот это тупо полученние от вк
    vk_id: int
    first_name: str
    last_name: str

# а это уже можно с выбором уника наверно и роли
class User(BaseModel):
    unik:str
    rol:str
    id: int # по чему индефицируем

class Role(str, Enum):
    stutent = 'student'
    teacher = "teacher"
    headman = "headman"

class User(BaseModel):
    id: int
    name: str
    role: Role

class Visit(BaseModel):
    id_visit: int
    name_visit: str
    visits: bool

class Lesson(BaseModel):
    id: int
    name_lesson: str
    data_created: date # вот это я прям сам без нейронки чувствую себя бил гейтсом

class UniversityEnum(str, Enum):
    MSU = "МГУ им. М.В. Ломоносова"
    MPEI = "МЭИ"
    MIPT = "МФТИ"

class UserInput(BaseModel):
    university: UniversityEnum

#УЖЕ НАЧИНАТЬ РАБОАТЬ С БАЗОЙ ДАННЫХ sql alchimy
    created_by: int #кто создал староста или препод


