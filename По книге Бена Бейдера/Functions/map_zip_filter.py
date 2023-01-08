from functools import reduce

lst_1 = ['4', '2', '3', '1', '0']
lst_2 = ['aa', 'bb', 'cc', 'dd', 'ee']
lst_3 = [2, 4, 5, 1, 3]

print(lst_1)  # ['4', '2', '3', '1', '0']
lst_1 = list(map(int, lst_1))
print(lst_1)  # [4, 2, 3, 1, 0]

exp = lambda x: x.sort()
exp(lst_1)
exp(lst_2)
exp(lst_3)  # [1, 2, 3, 4, 5]
print(lst_1)  # [0, 1, 2, 3, 4]

lst_1_lst_3_sum = list(map(lambda x, y: x + y, lst_1, lst_3))
print(lst_1_lst_3_sum)  # [1, 3, 5, 7, 9]

lst_2_case = list(map(str.capitalize, lst_2))
print(lst_2_case)  # ['Aa', 'Bb', 'Cc', 'Dd', 'Ee']

lst_1_filtered = list(filter(lambda x: x > 2, lst_1))
print(lst_1_filtered)  # [3, 4]

lst_3_reduce = reduce(lambda x, y: x + y, lst_3)
print(lst_3_reduce)  # 15

lst_1_lst_2_zip = list(zip(lst_2, lst_1))
print(lst_1_lst_2_zip)  # [('aa', 0), ('bb', 1), ('cc', 2), ('dd', 3), ('ee', 4)]
