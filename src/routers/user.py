from src.services.user import create_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.schemas.data import UserCreate, UserResponse
from src.models.data import User

router = APIRouter()

@router.post("/rooms/{room_id}/users", response_model=UserResponse)
def user_create(room_id: int, payload: UserCreate, db: Session = Depends(get_db)):
    created_user = create_user(room_id=room_id, payload=payload, db=db)
    
    if not created_user:
        raise HTTPException(status_code=404)
    
    return created_user

@router.get("/users{user_id}/target")
def get_my_target(user_id: int, db: Session = Depends(get_db)):
    me = db.query(User).filter(User.id == user_id).first()
    if not me:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    target_user = db.query(User).filter(User.id == me.target_id).first()
    
    if me.target_id is None:
        return {"message": "Игра еще не началась." }
    
    return {
        "your_name": me.username,
        "you_are_gifting_to": target_user.username
    }
        
    
