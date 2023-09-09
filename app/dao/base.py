from sqlalchemy import delete, insert, select, update

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def get_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=id)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model)
            data = await session.execute(query)
            await session.commit()
            return data.scalar()

    @classmethod
    async def multiple_add(cls, data: list):
        # для скрипта create_db.py
        async with async_session_maker() as session:
            query = insert(cls.model).values(data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_all(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter)
            data = await session.execute(query)
            return data.mappings().all()

    @classmethod
    async def update(cls, id: int, **data):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == id).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, id: int):
        async with async_session_maker() as session:
            row = delete(cls.model).where(cls.model.id == id)
            await session.execute(row)
            await session.commit()
