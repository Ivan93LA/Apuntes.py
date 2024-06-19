#Funciones

def mi_funcion ():
    print("Esto es una funcion")

mi_funcion ()

#suma de valores
def suma_dos_valores (primer_numero, segundo_numero):
    print(primer_numero + segundo_numero)
suma_dos_valores (6, 10)
suma_dos_valores (3232323 , 23232)
suma_dos_valores("Ivan", "Leon")
suma_dos_valores(1.3, 2.3)

def suma_dos_valores_conRetorno (primer_numero, segundo_numero):
    mi_suma = primer_numero + segundo_numero
    return mi_suma

mi_resultado = suma_dos_valores_conRetorno (10, 5)
mi_resultado = suma_dos_valores (1.4 , 5.2)

def print_name (name, surname):
    print(f"{name} {surname}") #f sirve para acceder a los valores

print_name(surname = "Leon", name= "Ivan")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Ivan", "Leon")
print_name_with_default("Ivan", "Leon", "Iv93")

def print_upper_texts(*texts): #El asterisco permite meter todos los prámetros que queramos
    for text in texts:
        print(text.upper())
        
print_upper_texts("Prueba", "Python", "Ivan")