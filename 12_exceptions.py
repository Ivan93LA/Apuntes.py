#Excepciones


numberOne = 5
numberTwo = 10
#numberTwo = "10" #Python no entiende el error con esta excepción


#Ejemplo de try except
try:
    print (numberOne + numberTwo)
    print("No se ha producido un error")
except:
    #Se ejecuta si se produce una excepcion
    print ("Se ha producido un error")

#jemplo de try except else
try:
    print (numberOne + numberTwo)
    print("No Se ha producido un error")
except:
    print ("Se ha producido un error")
else:
    #Esta linea se produce si no ha tenido errores los anteriores
    print("La ejecucción continua correctamente") 
finally:
    print("La ejecución continúa")

