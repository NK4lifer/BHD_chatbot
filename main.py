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
    #response = chatbot.get_response(user_input)
    # step 1: call api ollama localhost:15000/api/embed -> "vector of user_input"
    # step2: "vector of user_input" query mongodb and us consine -> get top 5 row
    # step3: build system prompt use top 5 row -> system prompt
    # step4: build user prompt use "user_input" -> user prompt
    # step5: call ollama api/generate { system prompt, user prompt}
    # step6: response of ollama -> process text json abit then  return {"response": response}
    pass

@app.get("/movie/{title}")
def get_movie(title: str):
    synopsis = chatbot.get_movie_synopsis(title)
    if synopsis =="Movie not found.":
        return '404'
    else: 
        return {"synopsis": synopsis}
# To run the app, use: uvicorn main:app --reload

import uvicorn

def runUvicorn(port):
    uvicorn.run(app, host="0.0.0.0", port=int(port), log_level="info")


if __name__ == "__main__":
    runUvicorn(8080)
