from app.dao.base import BaseDAO
from app.restaurants.models import Restaurant


class RestaurantDAO(BaseDAO):
    model = Restaurant
