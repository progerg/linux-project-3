import json

from fastapi import FastAPI
import random

app = FastAPI()

quotes = json.load(open("quotes.json"))


@app.get("/quote")
def get_quote():
    return random.choice(quotes)
