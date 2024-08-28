from fastapi import FastAPI
from routers import products , users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI () #Instanciar

#Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(users_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/") #Un get a un lugar 
async def root(): #Siempre tiene que ser asincrona
    return "Hola Trufhina"

@app.get("/url") #Un get a un lugar 
async def url(): #Siempre tiene que ser asincrona
    return "https://www.marca.com/"

#Iniciar un servidor con  uvicorn main:app --reload
#Importante no olvidar este paso 