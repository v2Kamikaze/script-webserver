"""
This module implements a simple FastAPI web server.
"""

from typing import Dict
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")

counter: Dict[str, int] = {}


class AddNumberRequest(BaseModel):
    """
    Modelo para inserir um número.
    """

    value: str


class AddNumberResponse(BaseModel):
    """
    Modelo para inserir um número.
    """

    value: str
    count: int


@app.post("/api/num/submit")
async def add_value(request: AddNumberRequest):
    """
    Endpoint para adicionar um número.
    """

    value = request.value

    if value in counter:
        counter[value] += 1
    else:
        counter[value] = 1

    return AddNumberResponse(value=value, count=counter[value])


@app.get("/", response_class=FileResponse)
async def serve_index():
    """
    Endpoint para servir o arquivo index.html.
    """
    return FileResponse("static/index.html")
