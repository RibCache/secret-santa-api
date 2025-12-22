from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.db.database import Base
from typing import list

class Room(Base):
    __tablename__ = "rooms"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    room_name: Mapped[str] = mapped_column()
    
    users: Mapped[list["User"]] = relationship(back_populates="room")
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column()
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    room: Mapped["Room"] = relationship(back_populates="users")