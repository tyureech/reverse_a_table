from pydantic import BaseModel


class SRestaurant(BaseModel):
    name: str
