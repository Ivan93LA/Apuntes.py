from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI () #Instanciar 


#Entidad user
class User(BaseModel): 
    name: str
    surname: str
    url: str
    age: int

users_list = [ User(name="Ivan", surname="Leon", url="https://www.mercadona.es/", age=31 ),
               User(name="Paula", surname="Ayuga",url="https://www.mercadona.es/" , age=25 ),
               User(name="Francisco", surname="Leon",url="https://www.mercadona.es/", age=54 )]
"""Hacer las listas son much mas rápidas y mejores"""

#Iniciar un servidor con  uvicorn users:app --reload
@app.get("/usersjson") #Un get a un lugar 
async def usersjson(): #Siempre tiene que ser asincrona
    return [{"name": "Ivan", "Surname": "Leon", "url": "https://www.mercadona.es/", "age": 31},
            {"name": "Paula", "Surname": "Ayuga", "url": "https://www.mercadona.es/", "age": 25},
            {"name": "Francisco", "Surname": "Leon", "url": "https://www.mercadona.es/", "age": 54}]

@app.get("/users") 
async def users(): 
    return users_list