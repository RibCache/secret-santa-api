from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.schemas.data import RoomCreate
from src.services.room import create_room, shuffle

router = APIRouter(prefix="/rooms")

@router.post("/")
def room_create(payload: RoomCreate, db: Session = Depends(get_db)):
    created_room = create_room(payload, db)
    return created_room

@router.post("/shuffle")
def shuffle_users(room_id: int, db: Session = Depends(get_db)):
    result = shuffle(room_id, db)
    return result