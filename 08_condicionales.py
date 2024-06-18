##condicionales


mi_condicion = False 

if mi_condicion :
    print ("Se ejecuta la condicion del if")

mi_condicion = 5 * 5    


if mi_condicion == 10 :
    print ("Se ejecuta la condicion del segundo if")

if mi_condicion > 10 and mi_condicion < 20 :
    print ("Es mayor que 10 y menor que 20")
elif mi_condicion == 25:
     print ("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


print("La ejecucion continua")

mi_string = "Mi cadena de texto"


if not mi_string:
    print("Mi cadena de texto no es vacía")
if mi_string:
    print("Mi cadena de texto no es vacía")