from src.schemas.data import RoomCreate
from src.models import data
from sqlalchemy.orm import Session

def create_room(payload: RoomCreate, db: Session):
    db_room = db.query(data.Room).filter(data.Room.room_name == payload.room_name).first()
    
    if db_room:
        return None
    
    new_room = data.Room(room_name = payload.room_name)
    
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    
    return new_room
    