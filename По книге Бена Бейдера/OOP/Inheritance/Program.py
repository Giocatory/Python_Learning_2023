from Class_Dog import Dog
from JackRussellTerrier import JackRussellTerrier
from Bulldog import Bulldog


def main():
    first_dog = JackRussellTerrier("Jack", 3)
    second_dog = Bulldog("Bullet", 4)

    print(f"{first_dog}. {first_dog.speak()}")  # Dog: Jack and 3 years. Jack say GRRRRR
    print(f"{second_dog}. {second_dog.speak()}")  # Bulldog: Bullet and 4 years. Bullet say 'Woof, Woof'

    print(isinstance(first_dog, Dog))  # True


if __name__ == "__main__":
    main()
