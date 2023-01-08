Length = len
print(Length("word"))  # 4


# Factorial function recursive
def Factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    else:
        return Factorial(num - 1) * num


def Factorial_Two(num: int) -> int:
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


print(Factorial_Two(5))  # 120
print(Factorial(5))  # 120


# print dictionary
def print_dict(dictionary: dict):
    for k, v in dictionary.items():
        print(f"{k} => {v}", end='\n')


print(print_dict({"one": 1, "two": 2}))
"""
one => 1
two => 2
"""


# lambda function
def outer_func(a, b, c):
    # def inner_func(x):
    #     return a * (x**2) + b * x + c
    # return inner_func
    return lambda x: a * (x ** 2) + b * x + c


print(outer_func(1, 2, 3)(4))  # 27 (ax2 + bx + c = 0 => x-?)
