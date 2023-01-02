from Class_Dog import Dog


class JackRussellTerrier(Dog):

    def __init__(self, name, age):
        Dog.__init__(self, name, age)

    def speak(self):
        return f"{self._get_name()} say GRRRRR"

