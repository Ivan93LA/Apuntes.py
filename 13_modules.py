#Módules

import my_module

my_module.sumValue (3, 1, 1) #Hay que escribir "module" para llamar al otro archivo
my_module.printValue("Hola Python")

from my_module import sumValue, printValue

sumValue( 3, 3, 4)
printValue ("Hola piton")

import math

print(math.pi) #Da acceso al valor pi
print(math.pow(2, 8)) #2 elevado a 8

from math import pi as NumeroPi #Renombrado
print(NumeroPi)



