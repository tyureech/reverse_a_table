from fastapi import APIRouter, status

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.bookings.utils import check_time_interval, validate_booking

router = APIRouter(prefix="/bookings", tags=["Бронирование"])


@router.post("/add/", status_code=status.HTTP_201_CREATED)
async def add_bookings(booking: SBooking):
    check_time_interval(booking.date, booking.time_from, booking.time_to)

    await validate_booking(
        booking.user_id,
        booking.restaurant_id,
    )

    tables_left = await BookingDAO.find_tables_left(
        restaurant_id=booking.restaurant_id,
        date=booking.date,
        time_from=booking.time_from,
        time_to=booking.time_to,
        persons=booking.persons,
    )

    booking_added = await BookingDAO.add(
        table_id=tables_left[0]["id"],
        user_id=booking.user_id,
        restaurant_id=booking.restaurant_id,
        date=booking.date,
        time_from=booking.time_from,
        time_to=booking.time_to,
        persons=booking.persons,
    )
    return booking_added


@router.get("/")
async def get_all_bookings():
    return await BookingDAO.get_all()


@router.get("/detail/{id}")
async def get_booking(id: int):
    return await BookingDAO.get_by_id(id=id)


# TODO
@router.put("/update/{id}")
async def update_bookings(id: int, booking: SBooking):
    check_time_interval(booking.date, booking.time_from, booking.time_to)

    await validate_booking(
        booking.user_id,
        booking.restaurant_id,
        booking.persons,
    )

    tables_left = await BookingDAO.find_tables_left(
        restaurant_id=booking.restaurant_id,
        date=booking.date,
        time_from=booking.time_from,
        time_to=booking.time_to,
        persons=booking.persons,
    )
    await BookingDAO.update(
        id=id,
        user_id=booking.user_id,
        table_id=tables_left[0]["id"],
        date=booking.date,
        time_from=booking.time_from,
        time_to=booking.time_to,
        persons=booking.persons,
    )
    return tables_left


@router.delete("/delete/{id}")
async def delete_bookings(id: int):
    return await BookingDAO.delete(id=id)
