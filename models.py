# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    Genders,
    validator
)

class UserBase(BaseModel):
    user_id: UUID  = Field(...)
    user_name: str = Field(
        ...,
        min_length=3,
        max_length=10,
        example='sgewux'
    )
    email: EmailStr = Field(..., example='sebas@sebas.com')
    birth_date: date = Field(..., example='1998-06-23')

    @validator('birth_date')  # Aqui está la magia
    def is_over_eighteen(cls, v):
        todays_date = date.today()
        delta = todays_date - v

        if delta.days/365 <= 18:
            raise ValueError('Must be over 18!')
        else:
            return v


class UserLogin(UserBase):
    password: str = Field(..., min_length=8)


class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)


class Tweet(BaseModel):
    pass