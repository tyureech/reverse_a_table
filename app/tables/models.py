from sqlalchemy import Column, Date, Integer, Time, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(
        ForeignKey("restaurants.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    number_seats = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

    restaurant = relationship("Restaurant", back_populates="table")
    booking = relationship("Booking", back_populates="table", cascade='all, delete')

    def __str__(self) -> str:
        return f"{self.quantity} столиков на {self.number_seats} места"
