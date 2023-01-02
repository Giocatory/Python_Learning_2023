import copy

colors = ["red", "green", "blue"]

# Вставить элемент в указанное место
colors.insert(3, "blue")
print(*colors, sep=', ')  # red, green, blue, blue

# Колличество вхождений
print(colors.count("blue"))  # 2

# Вставить элемент в конец
colors.append("violet")
print(*colors, sep=', ')  # red, green, blue, blue, violet

# Забрать и вернуть элемент
blue = colors.pop(2)  # pop забирает и возращает элемент, если с аргументом, то не должно превышать длину списка
print(blue)  # blue
print(*colors, sep=', ')  # red, green, blue, violet

colors.pop()
print(*colors, sep=', ')  # red, green, blue

# добавление нескольких элементов
colors.extend(["black", "white", "gray"])
print(*colors, sep=', ')  # red, green, blue, black, white, gray

# Копирование списков
# 1 slice
new_colors = colors[:]  # Поверхностное копирование
print(new_colors)  # ['red', 'green', 'blue', 'black', 'white', 'gray']
# 2 import copy
new_colors = copy.deepcopy(colors)
print(new_colors)  # ['red', 'green', 'blue', 'black', 'white', 'gray']

# Сортировка
colors.sort()
print(colors)  # ['black', 'blue', 'gray', 'green', 'red', 'white']
colors.sort(key=len)
print(colors)  # ['red', 'blue', 'gray', 'black', 'green', 'white']
