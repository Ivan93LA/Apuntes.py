from pydantic import BaseModel

class User(BaseModel): 
    id: str | None #Esto hace que sea opcional
    username: str
    email: str