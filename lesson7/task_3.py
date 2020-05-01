# Массив размером 2m + 1, где m — натуральное число,
# заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).
import random

def mediana(array):
    for idx in range(len(array)):
        left = 0
        right = 0
        replay = -1

        for item in array:
            if array[idx] > item:
                left += 1

            elif array[idx] < item:
                right += 1

            else:
                replay += 1

        # print(f'left={left}, right={right}, replay={replay}')
        if right > left:
            difference = right - left
        elif right < left:
            difference = left - right
        else:
            difference = 'Переменная не понадобилась'

        if left == right or left == replay + right \
                or right == replay + left or difference < replay:
            return array[idx]

# array = [10, 0, 10, 6, 8, 5, 6, 2, 4, 4, 8, 10, 4, 3, 10]
# array = [8, 4, 9, 0, 1, 2, 0, 2, 6, 5, 4, 2, 1, 3, 7, 2, 1]
# array = [6, 4, 6, 6, 10, 5, 6]
# array = [9, 7, 7, 3, 1, 10, 8, 0, 8, 0, 4, 0, 7, 6, 8, 8, 7]
array = [random.randint(0, 10) for _ in range((2*random.randint(1, 9)) + 1)]
print(array)
# print(sorted(array))

print(mediana(array))
