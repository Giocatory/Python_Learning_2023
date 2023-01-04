class Dog:
    __dogs_created = 0

    def __init__(self, name="No-name", age="No-age"):
        self.__name = name
        self.__age = age
        Dog.__dogs_created += 1

    @classmethod
    def how_many_dogs_created(cls):
        return cls.__dogs_created

    def __str__(self):
        return f"Dog: {self.__name} and {self.__age} years"

    # def get_name(self):
    #     return self.__name
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 < value < 30:
            self.__age = value
