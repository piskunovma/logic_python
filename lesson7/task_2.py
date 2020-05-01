# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

def my_func_sorted(arr):
    result = []

    if len(arr) <= 1:
        return arr

    centre = len(arr) // 2

    left = my_func_sorted(arr[:centre])
    right = my_func_sorted(arr[centre:])

    left_length, right_length = len(left), len(right)
    r_idx = 0
    l_idx = 0

    for _ in range(len(arr)):
        if l_idx < left_length and r_idx < right_length:

            if left[l_idx] <= right[r_idx]:
                result.append(left[l_idx])
                # print(result)
                l_idx += 1

            else:
                result.append(right[r_idx])
                # print(result)
                r_idx += 1

        elif l_idx == left_length:
            result.append(right[r_idx])
            # print(result)
            r_idx += 1

        elif r_idx == right_length:
            result.append(left[l_idx])
            # print(result)
            l_idx += 1

    return result


array = [float('{:.1f}'.format(random.uniform(0, 49.9))) for _ in range(10)]
print(array)

print(my_func_sorted(array))
