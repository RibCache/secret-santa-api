from src.services.user import create_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.schemas.data import UserCreate, UserResponse

router = APIRouter()

@router.post("/rooms/{room_id}/users", response_model=UserResponse)
def user_create(room_id: int, payload: UserCreate, db: Session = Depends(get_db)):
    created_user = create_user(room_id=room_id, payload=payload, db=db)
    
    if not created_user:
        raise HTTPException(status_code=404)
    
    return created_user
        
    
