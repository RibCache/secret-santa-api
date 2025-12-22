from fastapi import FastAPI
from src.routers.room import router as room
from src.db.database import Base,engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(engine)
    

app.include_router(room)