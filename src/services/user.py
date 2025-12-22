from fastapi import Depends
from sqlalchemy.orm import Session
from src.schemas.data import RoomCreate, UserCreate
from src.models import data

def create_user(room_id: int, payload: UserCreate, db: Session):
    room = db.query(data.Room).filter(data.Room.id == room_id).first()
    
    if not room:
        return None
    
    user = data.User(username = payload.username, room_id = room_id)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    