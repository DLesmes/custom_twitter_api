# Python
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional

# Pydantic
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    validator
)

class UserBase(BaseModel):
    user_id: UUID  = Field(...)
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
    password: str = Field(
        ...,
        min_length=8
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

    class Config: 
        schema_extra = {
            "example": {
                "user_id":"0023f7f1-e05a-4bd7-9099-8503e3523444",
                "first_name": "Jim",
                "last_name": "Rogers",
                "birth_date": "1998-06-23",
                "email": "jim.rogers@mail.com",
                "password": "asdfghtyy"
            }
        }

class UserRegister(User, UserLogin):
    pass

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ..., 
        min_length=1, 
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)