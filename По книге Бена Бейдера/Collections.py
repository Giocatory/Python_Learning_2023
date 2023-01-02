a, b, c, d = [], {}, (), {1, 2, 3}
print(type(a))  # <class 'list'>
print(type(b))  # <class 'dict'>
print(type(c))  # <class 'tuple'>
print(type(d))  # <class 'set'>


def return_tuple():
    return 1, 2, 3


print(type(return_tuple()))  # <class 'tuple'>
