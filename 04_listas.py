#istas

my_list = list()
my_other_list = []

#esto es para añadir elementos


my_list = [35, 25, 65, 22, 18]
print(my_list)
print(len(my_list)) 


my_other_list = [31, 1.68, "Ivan", "Leon"]
print(my_other_list)
print(type(my_other_list))


print(my_other_list[0])
print(my_other_list[2])
print(my_other_list[-1])
print(my_other_list.count("Ivan")) #cuenta cuantos elementos repetidos hay
print(my_list.count(22))

age, height, name, surname  = my_other_list
print(surname)

print(my_list + my_other_list)
my_other_list.append("La empresa")
print(my_other_list)
my_other_list.remove("La empresa")
print(my_other_list)

print(my_other_list.index("Ivan"))