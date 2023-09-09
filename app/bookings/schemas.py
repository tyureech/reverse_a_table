from datetime import date, time

from pydantic import BaseModel, Field, validator


class SBooking(BaseModel):
    user_id: int
    restaurant_id: int
    date: date
    time_from: time
    time_to: time
    persons: int = Field(ge=1, le=8)

    @validator("time_from", "time_to", pre=True)
    def remove_z_from_time(cls, value):
        if isinstance(value, str) and value.endswith("Z"):
            value = value[:-1]
        return value
