# В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

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

for i in range(len(arr_random)):
  if arr_random[i] == max:
    arr_random[i] = min
  elif arr_random[i] == min:
    arr_random[i] = max

# print(max, min)

print(arr_random)