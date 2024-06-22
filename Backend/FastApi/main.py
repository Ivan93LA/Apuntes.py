from fastapi import FastAPI

app = FastAPI () #Instanciar 

@app.get("/") #Un get a un lugar 
async def root(): #Siempre tiene que ser asincrona
    return "Hola Trufhina"

@app.get("/url") #Un get a un lugar 
async def url(): #Siempre tiene que ser asincrona
    return "https://www.marca.com/"

#Iniciar un servidor con  uvicorn main:app --reload