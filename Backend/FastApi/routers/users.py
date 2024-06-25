from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter () #Instanciar 


#Entidad user
class User(BaseModel): 
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [ User(id=1, name="Ivan", surname="Leon", url="https://www.mercadona.es/", age=31 ),
               User(id=2, name="Paula", surname="Ayuga",url="https://www.mercadona.es/" , age=25 ),
               User(id=3,name="Francisco", surname="Leon",url="https://www.mercadona.es/", age=54 )]
"""Hacer las listas son much mas rápidas y mejores"""

#Iniciar un servidor con  uvicorn users:app --reload
@router.get("/usersjson") #Un get a un lugar 
async def usersjson(): #Siempre tiene que ser asincrona
    return [{"name": "Ivan", "Surname": "Leon", "url": "https://www.mercadona.es/", "age": 31},
            {"name": "Paula", "Surname": "Ayuga", "url": "https://www.mercadona.es/", "age": 25},
            {"name": "Francisco", "Surname": "Leon", "url": "https://www.mercadona.es/", "age": 54}]

@router.get("/users") 
async def users(): 
    return users_list

#Path
@router.get("/user/{id}") #Pasar el parámetro del id
async def users(id: int): 
    return search_user(id)

    

 #Query   
@router.get("/userquery/") #Pasar el parámetro del id
async def users(id: int): 
   return search_user(id)

#Hacemos la funcion de la llamada con la comprobación try

@router.post("/user/")
async def user (user:User):
     if type(search_user(user.id)) == User:
         return {"Error": "El usuario ya existe"}
     else:
         users_list.append(user)
         return user

@router.put("/user/")
async def user(user:User): 
     
     found = False 
     for  index, saved_user in enumerate(users_list):
         if saved_user.id == user.id:
             users_list[index] = user
             found = True    
     if not found:
        return {"Error": "No se ha actualizado"}
     else:
        return user 

@router.delete("/user/{id}")
async def user(id:int): 

    for  index, saved_user in enumerate(users_list):
         if saved_user.id == id:
            del users_list[index] 
            found = True
            
    if not found:
        return {"Error": "No se ha eliminado el usuario"}


def search_user (id:int):
      users = filter(lambda user: user.id == id, users_list)
      try:
        return list(users)[0]
      except:
        return {"Error": "No se ha encontrado el usuario"}
      

