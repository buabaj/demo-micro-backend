from operator import mod
from turtle import mode
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


class Item(BaseModel):
    name: str
    email: str
    section: str

    class Config:
        orm_mode = True


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["Accept: application/json",
                   "Content-Type: application/json"],
    allow_credentials=True,
)

db = SessionLocal()


@app.get('/')
async def index():
    return {"message": "Mande landing page backend is active"}


@app.post('/add-user')
async def add_user(item: Item):

    if item.name == "" or item.email == "" or item.section == "":
        raise HTTPException(status_code=400, detail="Missing payload")
    if '@' not in item.email:
        raise HTTPException(status_code=400, detail="Email not valid")

    # delete user with email buabajerry@gmail.com
    # if it exists
    db.query(models.Waitlist).filter(
        models.Waitlist.email == "buabajerry@gmail.com").delete()
    db.commit()
    # check if email already in database
    if db.query(models.Waitlist).filter(models.Waitlist.email == item.email).first():
        raise HTTPException(
            status_code=400, detail="Email already in database")
    data = models.Waitlist(
        name=item.name, email=item.email, section=item.section)
    db.add(data)
    db.commit()
    db.close()
    return {"message": "User added to database"}


if __name__ == '__main__':
    uvicorn.run(app="app:app")
