from datetime import datetime, timedelta, time
import pytz

from app.exceptions import (
    FromOneToEightPersons,
    IncorrectInterva,
    MinimumIntervalOneHour,
    RestaurantIsOpenFrom09to23,
    RestaurantNotFound,
    UserNotFound,
)
from app.restaurants.dao import RestaurantDAO
from app.users.dao import UserDAO


def check_time_interval(date, time_from, time_to):
    closing_time = time(hour=23)
    opening_time = time(hour=9)
    if (
        time_from > closing_time
        or time_to > closing_time
        or time_from < opening_time
        or time_to < opening_time
    ):
        raise RestaurantIsOpenFrom09to23
    
    if time_from >= time_to:
        raise IncorrectInterva

    datetime_from = datetime.combine(date, time_from)
    datetime_to = datetime.combine(date, time_to)
    time_difference = datetime_to - datetime_from
    if time_difference <= timedelta(minutes=59):
        raise MinimumIntervalOneHour


async def validate_booking(user_id, restaurant_id):
    user = await UserDAO.get_by_id(user_id)
    if not user:
        raise UserNotFound

    restaurant = await RestaurantDAO.get_by_id(restaurant_id)
    if not restaurant:
        raise RestaurantNotFound
