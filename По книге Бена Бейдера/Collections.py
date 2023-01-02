a, b, c, d = [], {}, (), {1, 2, 3}
print(type(a))  # <class 'list'> => list()
print(type(b))  # <class 'dict'> => dict()
print(type(c))  # <class 'tuple'> не изменяемое => tuple()
print(type(d))  # <class 'set'> не изменяемое => set()


def return_tuple():
    return 1, 2, 3


print(type(return_tuple()))  # <class 'tuple'>

print(set("123123123"))  # {'3', '2', '1'} => всегда в разном порядке, но уникальные
print(list("123"))  # ['1', '2', '3']
print("A1; B1; C1".split("; "))  # ['A1', 'B1', 'C1']
print(tuple("123"))  # ('1', '2', '3')
