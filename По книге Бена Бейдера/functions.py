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
    for i in range(1, num+1):
        result *= i
    return result


print(Factorial_Two(5))  # 120
print(Factorial(5))  # 120


# function sum elements in list
def sum_elements(*args):
    return sum(args)


def sum_elements_list(args: list):
    return sum(args)


print(sum_elements(1, 2, 3, 4, 5))  # 15 (arguments numbers)
print(sum_elements_list([1, 2, 3, 4, 5]))  # 15 (arguments list)
