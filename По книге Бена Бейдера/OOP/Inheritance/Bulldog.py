from Class_Dog import Dog


class Bulldog(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        return f"{self._get_name()} say 'Woof, Woof'"

    def __str__(self):
        return f"Bulldog: {self._get_name()} and {self._get_age()} years"

