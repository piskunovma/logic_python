# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

arr1 = [random.randint(0, 100) for _ in range(0, random.randint(4, 10))]
print(arr1)

arr2 = []

i = 0
for itm in arr1:
    if arr1[i] % 2 == 0:
        arr2.append(i)
    i += 1

print(arr2)