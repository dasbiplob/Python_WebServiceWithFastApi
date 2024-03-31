from fastapi import Depends, FastAPI, Response, Form, Body
from fastapi.responses import RedirectResponse
from database import db
from models import Song

app = FastAPI()

_message = "world"

@app.get("/")
def hello():
    data = "Hello " + _message + "!"
    return Response(content=data, media_type="text/plain")

@app.post("/")
def set_message(message = Form(...)):
    global _message
    _message = message
    return RedirectResponse("/")

@app.get("/songs")
def get_songs(database_session = Depends(db)):
    return database_session.query(Song).all()

@app.post("/songs")
def add_song(name: str = Body(...), rating: int = Body(...), database_session = Depends(db)):
    song = Song(name = name, rating = rating)
    database_session.add(song)
    database_session.commit()
