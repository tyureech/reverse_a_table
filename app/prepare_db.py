from app.bookings.dao import BookingDAO
from app.bookings.models import Booking
from app.database import Base, engine
from app.restaurants.dao import RestaurantDAO
from app.restaurants.models import Restaurant
from app.tables.dao import TableDAO
from app.tables.models import Table
from app.users.dao import UserDAO
from app.users.models import User
from data.bookings import BOOKING_DATA
from data.restaurants import RESTUARANT_DATA
from data.tables import TABLE_DATA
from data.users import USER_DATA


async def recreate_db():
    async with engine.begin() as conn:
        print("delete tables")
        await conn.run_sync(Base.metadata.drop_all)
        print("create tables")
        await conn.run_sync(Base.metadata.create_all)

    print("insert data")
    await RestaurantDAO.multiple_add(RESTUARANT_DATA)
    await TableDAO.multiple_add(TABLE_DATA)
    await UserDAO.multiple_add(USER_DATA)
    await BookingDAO.multiple_add(BOOKING_DATA)
