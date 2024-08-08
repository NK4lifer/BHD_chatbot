# chat.py
import random
from database import Database

import random
import json

import torch

from model import NeuralNet
from nltk_util import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.95:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "I do not understand..."


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)

"""
class ChatBot:
    def __init__(self, db: Database):
        self.db = db

    def get_response(self, user_input: str):
        intents = self.db.get_intents()
        for intent in intents:
            if user_input.lower() in [pattern.lower() for pattern in intent["patterns"]]:
                return random.choice(intent["responses"])
        return "I don't understand that."

    def get_movie_synopsis(self, title: str):
        movie = self.db.get_movie_info(title)
        if movie:
            return movie.get("synopsis", "Synopsis not found.")
        return "Movie not found."

# Initialize the chatbot with the local database
local_db = Database("mongodb://localhost:27017", "local")
chatbot = ChatBot(local_db)

"""