from fastapi import APIRouter

from app.users.dao import UserDAO
from app.users.schemas import SUser

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.post(f"/add")
async def add_user(user: SUser):
    return await UserDAO.add(name=user.name, email=user.email)


@router.get("/")
async def get_users():
    return await UserDAO.get_all()


@router.get("/detail/{id}")
async def get_user(id: int):
    return await UserDAO.get_by_id(id=id)


@router.put("/update/{id}")
async def update_user(id: int, user: SUser):
    return await UserDAO.update(id=id, name=user.name, email=user.email)


@router.delete("/delete/{id}")
async def delete_user(id: int):
    return await UserDAO.delete(id=id)
