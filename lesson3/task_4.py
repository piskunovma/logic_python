# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


import random

arr_random = [random.randint(0, 100) for _ in range(0, random.randint(4, 10))]
print(arr_random)

min = arr_random[0]
max = arr_random[0]

for itm in arr_random:
    if itm > max:
        max = itm
    if itm < min:
        min = itm

i = 0
sum = 0

# Первый вариант
for idx in range(len(arr_random)):
    if arr_random[idx] == min or arr_random[idx] == max:
        idx += 1
        while arr_random[idx] != max and arr_random[idx] != min:
            sum = arr_random[idx] + sum
            idx += 1
        break

print(sum)

# Второй вариант
# sum2 = 0
#
# while arr_random[i] != max and arr_random[i] != min:
#     i += 1
#
# i += 1
#
# while arr_random[i] != max and arr_random[i] != min:
#     sum2 = arr_random[i] + sum2
#     i += 1
# #
# print(sum2)
