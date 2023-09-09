from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    booking = relationship("Booking", back_populates="user", cascade="all, delete")

    def __str__(self):
        return f"{self.name}, {self.email}"
