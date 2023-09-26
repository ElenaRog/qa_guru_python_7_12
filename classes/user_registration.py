from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Birthday:
    def __init__(self, value):
        self.day = datetime.strptime(value, '%d %B,%Y').day
        self.month = datetime.strptime(value, '%d %B,%Y').strftime('%B')
        self.year = datetime.strptime(value, '%d %B,%Y').year
        self.bday = value


class Hobbies(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    number: str
    date_of_birth: Birthday
    subject: str
    hobbies: Hobbies
    picture: str
    address: str
    state: str
    city: str
