from fastapi import FastAPI
from sqladmin import Admin

from app.admin.view import (
    BookingAdmin,
    UserAdmin,
    RestaurantAdmin,
    TableAdmin,
)
from app.bookings.routers import router as router_booking
from app.database import engine
from app.users.routers import router as router_user
from app.restaurants.routers import router as router_restaurant
from app.tables.routers import router as router_table

app = FastAPI()

app.include_router(router_booking)
app.include_router(router_restaurant)
app.include_router(router_user)
app.include_router(router_table)


admin = Admin(app, engine)
admin.add_view(RestaurantAdmin)
admin.add_view(TableAdmin)
admin.add_view(UserAdmin)
admin.add_view(BookingAdmin)

import sentry_sdk

sentry_sdk.init(
    dsn="https://cca6164ad48ec17cbf6843a4a3d0e5f8@o4505760277463040.ingest.sentry.io/4505839246835712",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
