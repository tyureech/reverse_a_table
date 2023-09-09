from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Restaurant(Base):
    __tablename__ = "restaurants" 
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)

    table = relationship("Table", back_populates="restaurant", cascade='all, delete')

    def __str__(self):
        return f"{self.name}"
