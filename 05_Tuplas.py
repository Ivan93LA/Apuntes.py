##Tuplas
#A diferencia de la lista, las tuplas NO se pueden modificar ni aumentar/reducir

mi_tupla = tuple()
mi_otra_tupla = ()


mi_tupla = (31, 1.68, "Ivan", "Leon")
mi_otra_tupla = (9, 23 ,23 ,54)
print( mi_tupla )
print(type(mi_tupla))

print(mi_tupla[0])
print(mi_tupla[-1])

print(mi_tupla.count("Ivan"))
print(mi_tupla.index("Ivan"))

print(mi_tupla)

mi_sum_tupla = mi_tupla + mi_otra_tupla
print(mi_sum_tupla)
print(mi_sum_tupla[3:6]) #Para poner un trozo de la tupla

#truco para reasingnar tupla/lista
mi_tupla = list(mi_tupla)
print(type(mi_tupla))

mi_tupla[3] = "Sally Corporation"
mi_tupla.insert(1, "Verde")
mi_tupla=tuple(mi_tupla)
print(tuple(mi_tupla))
print(type(mi_tupla))


"""Esto lo que hace es borrar la variable
del mi_tupla
print(mi_tupla)"""