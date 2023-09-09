from sqlalchemy import select, and_, or_, insert
from sqlalchemy.sql.functions import count
from app.bookings.models import Booking
from app.dao.base import BaseDAO
from app.exceptions import TableFullyBooked, TableNotFoundRestaurant
from app.tables.models import Table
from app.database import async_session_maker, engine


class BookingDAO(BaseDAO):
    model = Booking

    @classmethod
    async def find_tables_left(cls, restaurant_id, date, time_from, time_to, persons):
        """
        select tables.id, tables.quantity - count(bookings.*) from bookings
        left join tables
        on bookings.table_id = tables.id
        where date = '2012-12-12'
        and tables.number_seats = 4
        and tables.restaurant_id = 1
        and (
            (time_from >= '10:30:00' and time_from <= '14:00:00')
            or (time_from <= '10:30:00' and time_to >= '10:30:00')
        )
        group by tables.id, tables.quantity
        """
        async with async_session_maker() as session:
            # если персон 3 будет выделен столик на 4 человека, если 5 - то на 6 и тд
            number_seats = persons + 1 if persons % 2 == 1 else persons

            # проверка на свободные столы в ресторане в заданном интервале
            query_tables_left = (
                select(
                    Table.id,
                    Table.number_seats,
                    (Table.quantity - count()).label("quantity"),
                )
                .select_from(Booking)
                .join_from(Booking, Table, Booking.table_id == Table.id, isouter=True)
                .where(
                    and_(
                        Booking.date == date,
                        Table.number_seats == number_seats,
                        Table.restaurant_id == restaurant_id,
                        or_(
                            and_(
                                Booking.time_from >= time_from,
                                Booking.time_from < time_to,
                            ),
                            and_(
                                Booking.time_from <= time_from,
                                Booking.time_to > time_from,
                            ),
                        ),
                    )
                )
                .group_by(Table.id, Table.quantity)
            )
            # print(query_tables_left.compile(engine, compile_kwargs={"literal_binds": True}))
            table_left = await session.execute(query_tables_left)
            #TODO 
            table_data = table_left.mappings().all()
            # если таблица не существует значит все столы свободны
            if not table_data:
                query_table = select(Table.__table__.columns).where(
                    Table.restaurant_id == restaurant_id,
                    Table.number_seats == number_seats,
                )
                table = await session.execute(query_table)
                table_data = table.mappings().all()
                if not table_data:
                    raise TableNotFoundRestaurant
            if table_data[0]["quantity"] <= 0:
                raise TableFullyBooked
            return table_data


    @classmethod
    async def add(cls, table_id, user_id, restaurant_id, date, time_from, time_to, persons):

        async with async_session_maker() as session:
            add_booking = (
                insert(Booking)
                .values(
                    user_id=user_id,
                    table_id=table_id,
                    persons=persons,
                    date=date,
                    time_from=time_from,
                    time_to=time_to,
                )
                .returning(Booking.__table__.columns)
            )
            booking = await session.execute(add_booking)
            await session.commit()
            booking_data = dict(booking.mappings().one())
            booking_data.update({"restaurant_id": restaurant_id})
            return booking_data

