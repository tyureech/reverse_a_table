from fastapi import APIRouter

from app.tables.dao import TableDAO
from app.tables.schemas import STable

router = APIRouter(prefix="/tables", tags=["Столики"])


@router.post(f"/add")
async def add_table(table: STable):
    return await TableDAO.add(
        restaurant_id=table.restaurant_id,
        number_seats=table.number_seats,
        quantity=table.quantity,
    )


@router.get(f"/")
async def get_all_tables():
    return await TableDAO().get_all()


@router.get("/detail/{id}")
async def get_table(id: int):
    return await TableDAO.get_by_id(id=id)


@router.put("/update/{id}")
async def update_table(id: int, table: STable):
    return await TableDAO.update(
        id=id,
        restaurant_id=table.restaurant_id,
        number_seats=table.number_seats,
        quantity=table.quantity,
    )


@router.delete("/delete/{id}")
async def delete_table(id: int):
    return await TableDAO.delete(id=id)
