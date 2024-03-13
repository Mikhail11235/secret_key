from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date, datetime, timedelta
from typing import Optional


EXPIRED_AT_7_DAY = 0
EXPIRED_AT_5_MIN = 1
EXPIRED_AT_30_MIN = 2
EXPIRED_AT_1_HOUR = 3
EXPIRED_AT_12_HOUR = 4
EXPIRED_AT_1_DAY = 5
EXPIRED_AT_3_DAY = 6


class ShowSecret(BaseModel):
    secret: str


class ShowKey(BaseModel):
    key: str
    expired_at: date


class CreateSecret(BaseModel):
    email: EmailStr = Field(...)
    secret: str
    expired_at: int
    key: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "email": "hobby@horsing.com",
                "secret": "I love hobby horsing",
                "expired_at": 0
            }
        }

    @validator("key")
    def сheck_key(cls, value):
        if value is None:
            raise ValueError("key: may not be None")
        if len(value) < 5:
            raise ValueError("key: is too short")
        return value

    @validator("secret")
    def check_bad_words(cls, value):
        for bad_word in ("fck", "put in", "cucumber"):
            if bad_word in value.lower():
                raise ValueError(f"Bad word \"{bad_word}\" detected...")
        return value

    @validator("expired_at")
    def check_and_reformat_expired_at(cls, value):
        if value == EXPIRED_AT_7_DAY:
            value = datetime.utcnow() + timedelta(days=7)
        elif value == EXPIRED_AT_5_MIN:
            value = datetime.utcnow() + timedelta(minutes=5)
        elif value == EXPIRED_AT_30_MIN:
            value = datetime.utcnow() + timedelta(minutes=30)
        elif value == EXPIRED_AT_1_HOUR:
            value = datetime.utcnow() + timedelta(hours=1)
        elif value == EXPIRED_AT_12_HOUR:
            value = datetime.utcnow() + timedelta(hours=12)
        elif value == EXPIRED_AT_1_DAY:
            value = datetime.utcnow() + timedelta(days=1)
        else:
            raise ValueError("expired_at: invalid option")
        return value
