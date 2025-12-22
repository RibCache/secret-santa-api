from pydantic import BaseModel

class RoomCreate(BaseModel):
    room_name: str
    
class RoomResponse(BaseModel):
    id: int
    room_name: str
    
    class Config:
        from_attributes = True
    
    