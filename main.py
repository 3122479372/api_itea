from typing import Union
from connection import Connection

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/libros")
def consulta_todos_los_libros():   
    libros = Connection()
    total_libros = libros.consulta_libreria()
    return total_libros


@app.get("/autor/{autores}")
def consulta_todos_los_autores(autores:str):   
    autor = Connection()
    total_autor = autor.consulta_autor(autores)
    return total_autor


@app.get("/editorial/{edito}")
def consulta_todos_los_autores(edito:str):   
    autor = Connection()
    total_autor = autor.consulta_autor(edito    )
    return total_autor