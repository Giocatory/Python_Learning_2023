from Class_Dog import Dog

first_dog = Dog("Бобик", 3)
second_dog = Dog("Шарик", 4)

print(first_dog)  # Dog: Бобик and 3 years
print(first_dog.name)  # Бобик
first_dog.age = 5
print(first_dog.age)  # 5


print(second_dog)  # Dog: Шарик and 4 years
print(second_dog.age)  # 4

print(Dog.how_many_dogs_created())  # 2

# полной инкапсуляции нет
print(first_dog._Dog__age)  # 3, но так делать не рекомендуют

# Добавление произвольного атрибута, которого нет в классе
first_dog.color = "brown"
print(first_dog.color)  # brown
