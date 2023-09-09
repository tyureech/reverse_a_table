from sqlalchemy import Column, Date, Integer, Time, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship, backref

from app.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    table_id = Column(
        Integer,
        ForeignKey("tables.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    persons = Column(Integer, CheckConstraint("persons>1 and persons<9"), nullable=False)
    date = Column(Date, nullable=False)
    time_from = Column(Time, nullable=False)
    time_to = Column(Time, nullable=False)
    CheckConstraint("persons > 0 and persons < 9", name="persons")

    user = relationship("User", back_populates="booking")
    table = relationship("Table", back_populates="booking")

    def __str__(self) -> str:
        return f"#{self.id}, persons:{self.persons}"
