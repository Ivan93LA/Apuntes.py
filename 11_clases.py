#Clases

class MyEmptyPerson:
    pass

print(MyEmptyPerson())

class Person:
 def __init__(self, name, surname, alias = "sin alias"): #Es un constructor de clase en Python
        self.full_name = f"{name} {surname} {alias}"
 #Self es obligatorio SIEMPRE para el constructor   

 def walk (self):
    print (f"{self.full_name} Está caminando")
    #Acordarse de tabular las funciones para que funcionen

       
My_Person = Person("IVAN", "LEON")
print(My_Person.full_name)
My_Person.walk()

My_Other_Person = Person("Paula", "Ayuga", "Trufinha")
print(My_Other_Person.full_name)
My_Other_Person.walk()

My_Other_Person.full_name = "Federico Lopez (Gran persona)"
print(My_Other_Person.full_name)
My_Other_Person.walk()