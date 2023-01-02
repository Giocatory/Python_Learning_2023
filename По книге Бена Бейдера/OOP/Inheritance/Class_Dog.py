class Dog:

    def __init__(self, name="No-name", age="No-age"):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"Dog: {self.__name} and {self.__age} years"

    def _get_name(self):
        return self.__name

    def _get_age(self):
        return self.__age
