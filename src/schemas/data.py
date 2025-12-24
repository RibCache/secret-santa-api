from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    
    class Config:
        from_attributes = True

class RoomCreate(BaseModel):
    room_name: str
    
class RoomResponse(BaseModel):
    id: int
    username: str
    room_id: int
    target_id: int | None = None
    
    class Config:
        from_attributes = True
    
    