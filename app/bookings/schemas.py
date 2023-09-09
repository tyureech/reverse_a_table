from datetime import date, time
from datetime import time

from pydantic import BaseModel, validator, Field


class SBooking(BaseModel):
    user_id: int
    restaurant_id: int
    date: date
    time_from: time
    time_to: time
    persons: int = Field(ge=1, le=8)

    @validator('time_from', 'time_to', pre=True)
    def remove_z_from_time(cls, value):
        if isinstance(value, str) and value.endswith('Z'):
            print(value)
            value = value[:-1]
        return value
