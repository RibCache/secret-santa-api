from fastapi import Depends
from sqlalchemy.orm import Session
from src.schemas.data import RoomCreate, UserCreate
from src.models import data

def create_user(room_id: int, payload: UserCreate, db: Session):
    room = db.query(data.Room).filter(data.Room.id == room_id).first()
    
    if not room:
        return None
    
    existing_user = db.query(data.User).filter(
        data.User.room_id == room_id,
        data.User.username == payload.username
    ).first()

    if existing_user:
        raise ValueError(f"Пользователь с именем '{payload.username}' уже есть в этой комнате.")
    
    user = data.User(username = payload.username, room_id = room_id)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    