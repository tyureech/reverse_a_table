from pydantic import BaseModel, Field, validator


class STable(BaseModel):
    restaurant_id: int
    number_seats: int = Field(ge=1, le=8)
    quantity: int

    @validator("number_seats")
    def must_be_even(cls, value):
        if value % 2 != 0:
            raise ValueError('Число должно быть четным')
        return value
