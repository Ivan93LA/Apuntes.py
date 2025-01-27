from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema
from db.client import db_client

#Instanciar 

router = APIRouter (prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"mess1age": "No encontrado"}})

#Entidad user


users_list = []
"""Hacer las listas son mucho mas rápidas y mejores"""


@router.get("/") 
async def users(): 
    return users_list

#Path
@router.get("/{id}") #Pasar el parámetro del id
async def users(id: int): 
    return search_user(id)

    

 #Query   
@router.get("/") #Pasar el parámetro del id
async def users(id: int): 
   return search_user(id)

#Hacemos la funcion de la llamada con la comprobación try

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user (user:User):
 #    if type(search_user(user.id)) == User:
  #       return {"Error": "El usuario ya existe"}
     #else:

    user_dict = dict(user)
    del user_dict["id"]


    id = db_client.local.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.local.users.find_one({"_id" : id}))
    return User(**new_user)

@router.put("/")
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

@router.delete("/u{id}")
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
      

