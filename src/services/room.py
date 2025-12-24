from src.schemas.data import RoomCreate
from src.models import data
from sqlalchemy.orm import Session
import random

def create_room(payload: RoomCreate, db: Session):
    db_room = db.query(data.Room).filter(data.Room.room_name == payload.room_name).first()
    
    if db_room:
        return None
    
    new_room = data.Room(room_name = payload.room_name)
    
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    
    return new_room

def shuffle( room_id: int, db: Session):
    users = db.query(data.User).filter(data.User.room_id == room_id).all()
    
    if len(users) < 2:
        raise ValueError("В комнате должно быть минимум 2 человека")
    
    random.shuffle(users)
    
    for i in range(len(users) - 1):
        users[i].target_id = users[i + 1].id
    
    users[-1].target_id = users[0].id
        
    db.commit()
    
    return {"status": "ok", "message": "Тайный Санта распределил подарки!"}
        
    