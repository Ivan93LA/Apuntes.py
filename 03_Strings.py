#Strings

mi_string = "Mi String de ejemplo"
mi_otro_string = 'Otro ejemplo de string'

print (len(mi_otro_string))
print (len (mi_string + mi_otro_string))
print (mi_string + ' ' + mi_otro_string)

mi_nueva_linea = "Este es otro ejemplo \n con salto de linea"
print (mi_nueva_linea)

mi_scape_string = "\t primera frase \n segunda frase"
print(mi_scape_string) 

# Formateos

name , surname, age = "Ivan" , "Leon", "31"
print ("Mi nombre es: {} {} y mi edad es {}". format (name, surname, age))
print ("Mi nombre es: %s %s y mi edad es %s" %(name, surname, age))

#desempaquetado de caracteres
language = "python"
a , b, c, d, e, f= language
print (a)
print (e)


#division

language_slice = language[1:3]
print (language_slice)

language_slice = language[-2]
print (language_slice)

language_slice = language[0:6:2]
print (language_slice)

#revserse
reverse_language = language [::-1]
print (reverse_language)

#funciones
print(language.capitalize()) #pone la primera en mayúscula
print(language.upper()) #todas
print(language.count("t"))
print(language.isnumeric()) #si la variale es numérica
print(language.lower()) #minusculas
print(language.lower().isupper()) 
print(language.startswith("py")) 

