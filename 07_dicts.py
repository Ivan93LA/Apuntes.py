###Diccionarios
"""Son tipos de estructura en el 
que podemos almacenar datos de tipo clave-valor"""

mi_dict = dict()
mi_otro_dict = {}
print(type(mi_dict))
print(type(mi_otro_dict))

mi_otro_dict = {
    "Nombre" : "Ivan",
    "Apellido":"Leon",
    "edad" : 31,
    1:"Python"}

mi_dict = {
    "Nombre" : "Ivan", 
    "Apellido":"Leon", 
    "edad" : 31, 
    "Lenguajes":{"Python", "Java", "PHP"},
    1:1.68
    }

print(mi_otro_dict)
print(mi_dict)

print(len(mi_otro_dict))

print (mi_dict["Lenguajes"])

mi_dict["Nombre"] = "Paula"
print(mi_dict["Nombre"])

print("Nombre" in mi_dict) #esto es buscar por clave
print("Apellido" in mi_dict)

print(mi_dict.items())
print(mi_dict.keys())
print(mi_dict.values())
print(mi_dict.fromkeys(("Nombre", 1)))

my_new_dict = dict.fromkeys(("Nombre", 1 , "piso"))
print(my_new_dict)

