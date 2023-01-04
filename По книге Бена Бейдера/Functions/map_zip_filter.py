from functools import reduce

lst_1 = ['4', '2', '3', '1', '0']
lst_2 = ['a', 'b', 'c', 'd', 'e']
lst_3 = [2, 4, 5, 1, 3]

print(lst_1)  # ['4', '2', '3', '1', '0']
lst_1 = list(map(int, lst_1))
print(lst_1)  # [4, 2, 3, 1, 0]

s = lambda x: x.sort()
s(lst_1)
s(lst_2)
s(lst_3)  # [1, 2, 3, 4, 5]
print(lst_1)  # [0, 1, 2, 3, 4]

lst_1_lst_3_sum = list(map(lambda x, y: x + y, lst_1, lst_3))
print(lst_1_lst_3_sum)  # [1, 3, 5, 7, 9]

lst_1_filtered = list(filter(lambda x: x > 2, lst_1))
print(lst_1_filtered)  # [3, 4]

lst_3_reduce = reduce(lambda x, y: x + y, lst_3)
print(lst_3_reduce)  # 15

lst_1_lst_2_zip = list(zip(lst_2, lst_1))
print(lst_1_lst_2_zip)  # [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)]
