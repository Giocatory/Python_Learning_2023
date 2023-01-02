class Dog:
    dogs_created = 0

    def __init__(self, name="No-name", age="No-age"):
        self.__name = name
        self.__age = age
        Dog.dogs_created += 1

    def __str__(self):
        return f"Dog: {self.__name} and {self.__age} years"

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
