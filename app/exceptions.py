from fastapi import HTTPException, status

class BookingExceptions(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class TableFullyBooked(BookingExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Не осталось свободных столиков"

class UserNotFound(BookingExceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Пользователь не найден"

class RestaurantNotFound(BookingExceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Ресторан не найден"

class RestaurantNotFound(BookingExceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Ресторан не найден"

class TableNotFound(BookingExceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "столик не найден"

class MinimumIntervalOneHour(BookingExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Минимальный интервал бронирования 1 час"

class IncorrectInterva(BookingExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Некорректный интервал"

class FromOneToEightPersons(BookingExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Число персон должно быть от 1 до 8"

class TableNotFoundRestaurant(BookingExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Не найден столик в ресторане на данное количество человек"

class TableNotFoundRestaurant(BookingExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Не найден столик в ресторане на данное количество человек"


class RestaurantIsOpenFrom09to23(BookingExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Ресторан работает c 09:00 до 23:00"
