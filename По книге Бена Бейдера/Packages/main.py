from Example_package.first_module import *  # Squaring, AnaloguePow
from Example_package.second_module import Cube


def main():
    print(Squaring.__doc__)  # Возведение в квадрат
    print(Squaring(4))  # 16
    print(Cube.__doc__)  # Возведение в куб
    print(Cube(4))  # 64

    print(AnaloguePow(2, 8))  # 256


if __name__ == "__main__":
    main()
