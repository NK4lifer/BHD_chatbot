# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from chat import ChatBot
from database import Database

app = FastAPI()

# Initialize database and chatbot
intents_db = Database("mongodb://localhost:27017", "Intents_db")
movies_db = Database("mongodb://localhost:27017")
chatbot = ChatBot(intents_db, movies_db)

class ChatRequest(BaseModel):
    user_input: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the chatbot API"}

@app.post("/chat")
def chat(user_input: str):
    response = chatbot.get_response(user_input)
    return {"response": response}

@app.get("/movie/{title}")
def get_movie(title: str):
    synopsis = chatbot.get_movie_synopsis(title)
    if synopsis =="Movie not found.":
        return '404'
    else: 
        return {"synopsis": synopsis}
# To run the app, use: uvicorn main:app --reload
