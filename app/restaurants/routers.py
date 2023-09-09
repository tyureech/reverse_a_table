from fastapi import APIRouter

from app.restaurants.dao import RestaurantDAO
from app.restaurants.schemas import SRestaurant


router = APIRouter(prefix="/restaurant", tags=["Рестораны"])


@router.post(f"/add")
async def add_retaurants(restaurant: SRestaurant):
    return await RestaurantDAO.add(name=restaurant.name)


@router.get(f"/")
async def get_all_retaurants():
    return await RestaurantDAO.get_all()


@router.get("/detail/{id}")
async def get_retaurant(id: int):
    return await RestaurantDAO.get_by_id(id=id)


@router.put("/update/{id}")
async def update_restaurant(id: int, restaurant: SRestaurant):
    return await RestaurantDAO.update(id=id, name=restaurant.name)


@router.delete("/delete/{id}")
async def delete_retaurant(id: int):
    return await RestaurantDAO.delete(id=id)
