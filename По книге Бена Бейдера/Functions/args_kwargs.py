# function sum elements in list
def sum_elements(*args) -> int:
    return sum(args)


def sum_elements_list(args: list) -> int:
    return sum(args)


print(sum_elements(1, 2, 3, 4, 5))  # 15 (arguments numbers)
print(sum_elements_list([1, 2, 3, 4, 5]))  # 15 (arguments list)


def print_dict_any(**kwargs):
    print(kwargs)


print_dict_any(a=2, b=1, c=3)  # {'a': 2, 'b': 1, 'c': 3}
