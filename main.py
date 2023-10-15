import wikipedia
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Sumary(BaseModel):
    request: str

@app.get("/{request}")
def request(request):
    return Sumary(request= wikipedia.summary(request, sentences=5))


class Sumary2(BaseModel):
    results: str


@app.get('/sentences/')
def your_results(path: str, sencou: int):
    return Sumary2(results = wikipedia.summary(path, sentences=sencou, auto_suggest = False))


class Request(BaseModel):
    result: str
    quantity: int

class Summary3(BaseModel):
    text_from_wiki: List[str]

@app.post("/")
def many_results(many_results: Request):
    return Summary3(text_from_wiki=wikipedia.search(many_results.result, results = many_results.quantity))
