#Sets
mi_set = set()
mi_otro_set = {}

print(type(mi_otro_set)) #inicialmente es un diccionario

mi_otro_set = {"Ivan", "Leon", 31}
print(mi_otro_set)
print(type(mi_otro_set))

print(len(mi_otro_set))

mi_otro_set.add("Paula")


print(mi_otro_set)       # Un set no es una estructura ordenada
mi_otro_set.add("Paula") # El set no admite repetidos
print(mi_otro_set)

print("Ivaan" in mi_otro_set) #Esto es para realizar alguna busqueda
print("Ivan" in mi_otro_set)

mi_otro_set.remove("Ivan")
print(mi_otro_set)

mi_otro_set.clear()
print(mi_otro_set)
print(len(mi_otro_set))

mi_set = {"Paula", "Ayuga", 25}
mi_lista = list(mi_set)
print(mi_lista)
print(mi_lista[0])

mi_otro_set = {"PHP", "Java" ," Python"}
mi_nueva_set = mi_set.union(mi_otro_set)
print(mi_nueva_set)
print(mi_nueva_set.union(mi_nueva_set)) #Tampoco acepta repetidos como las tuplas
print(mi_nueva_set.union(mi_nueva_set).union({"Caca" , "Pis"}))

print(mi_nueva_set.difference(mi_set))