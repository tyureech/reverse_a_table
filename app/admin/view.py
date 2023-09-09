from sqladmin import ModelView

from app.bookings.models import Booking
from app.restaurants.models import Restaurant
from app.tables.models import Table
from app.users.models import User


class RestaurantAdmin(ModelView, model=Restaurant):
    column_list = "__all__"


class TableAdmin(ModelView, model=Table):
    column_list = "__all__"


class UserAdmin(ModelView, model=User):
    column_list = "__all__"


class BookingAdmin(ModelView, model=Booking):
    column_exclude_list = [Booking.table]
