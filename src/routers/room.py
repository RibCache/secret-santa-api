from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.schemas.data import RoomCreate
from src.services.room import create_room

router = APIRouter(prefix="/rooms")

@router.post("/")
def room_create(payload: RoomCreate, db: Session = Depends(get_db)):
    created_room = create_room(payload, db)
    return created_room