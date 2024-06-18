#bucles

mi_condicion = 0

while mi_condicion < 10:
    print(mi_condicion)  
    mi_condicion += 2
else:
    print("Mi condicion es mayor o igual que 10")
print("La ejecucion continua")

while mi_condicion < 20:
    mi_condicion +=1
    if mi_condicion == 15:
        print("Se detiene la ejecución")
        break
    print(mi_condicion)

print("La ejecucion continua")

#for
my_list = [35, 25, 65, 22, 18]

for element in my_list:
    print(element)

mi_tupla = (31, 1.68, "Ivan", "Leon")
for element in mi_tupla:
    print(element)

mi_set = {"Paula", "Ayuga", 25}
for element in mi_set:
    print(element)

mi_dict = {
    "Nombre" : "Ivan", 
    "Apellido":"Leon", 
    "edad" : 31, 
    "Lenguajes":{"Python", "Java", "PHP"},
    1:1.68
    }
for element in mi_dict:
    print(element)
    if element == "edad":
        continue
    else:
     print("Se ejecuta")
else:
    print("El bucle ha finalizado")
