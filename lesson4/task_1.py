# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.


# Выбрал задачу 6 из 3-го урока.

# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


import random
import timeit
import cProfile

# Первый вариант
def my_func_1(my_num):
    arr_random = [random.randint(0, 100) for _ in range(my_num)]
    # print(arr_random)

    min = arr_random[0]
    max = arr_random[0]

    for itm in arr_random:
        if itm > max:
            max = itm
        if itm < min:
            min = itm

    i = 0
    sum = 0

    for idx in range(len(arr_random)):
        if arr_random[idx] == min or arr_random[idx] == max:
            idx += 1
            while arr_random[idx] != max and arr_random[idx] != min:
                sum = arr_random[idx] + sum
                idx += 1
            break

    # print(sum)

# Второй вариант
def my_func_2(my_num):
    arr_random = [random.randint(0, 100) for _ in range(my_num)]
    # print(arr_random)

    min = arr_random[0]
    max = arr_random[0]

    for itm in arr_random:
        if itm > max:
            max = itm
        if itm < min:
            min = itm

    i = 0
    sum2 = 0
    while arr_random[i] != max and arr_random[i] != min:
        i += 1

    i += 1

    while arr_random[i] != max and arr_random[i] != min:
        sum2 = arr_random[i] + sum2
        i += 1

    # print(sum2)

# Третий вариант
def my_func_3(my_num):
    arr_random = [random.randint(0, 100) for _ in range(my_num)]
    # print(arr_random)

    min = arr_random[0]
    max = arr_random[0]

    for itm in arr_random:
        if itm < min:
            min = itm
        if itm > max:
            max = itm

    # print("max=", max)
    # print("min=", min)

    min_index = 0
    max_index = 0
    for idx in range(0, len(arr_random)):
        if arr_random[idx] is min:
            min_index = idx
        elif arr_random[idx] is max:
            max_index = idx

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    result = 0
    for idx in range(min_index + 1, max_index):
        result += arr_random[idx]

    # print("res=", result)

print(timeit.timeit('my_func_1(100)', number= 100, globals=globals())) # 0.016400134999999996
print(timeit.timeit('my_func_1(200)', number= 100, globals=globals())) # 0.029535391999999994
print(timeit.timeit('my_func_1(300)', number= 100, globals=globals())) # 0.043536749

print("*" * 30)

print(timeit.timeit('my_func_2(100)', number= 100, globals=globals())) # 0.016335076000000004
print(timeit.timeit('my_func_2(200)', number= 100, globals=globals())) # 0.02919089600000002
print(timeit.timeit('my_func_2(300)', number= 100, globals=globals())) # 0.04056878999999999

print("*" * 30)

print(timeit.timeit('my_func_3(100)', number= 100, globals=globals())) # 0.01452582400000002
print(timeit.timeit('my_func_3(200)', number= 100, globals=globals())) # 0.03310248399999999
print(timeit.timeit('my_func_3(300)', number= 100, globals=globals())) # 0.04144236899999998

print("*" * 300)
print("*" * 300)

# Проверил также на более больших цифрах. Добавил в комментарии строчки которые хоть как-то отличаются,
# остальные строки результата работы cProfile показывают одинаковые результаты во всех трех вариантах решения задачи.
cProfile.run('my_func_1(1000)') # 1267    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
print("*" * 300)
cProfile.run('my_func_2(1000)') # 1270    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
print("*" * 300)
cProfile.run('my_func_3(1000)') # 1227    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Вывод:
# Все три варианта решения имеют линейную асимптотику.
# Скорость выполнения примерно одинаковая во всех трех вариантах.
# Совсем немного стабильнее отрабатывает второй вариант(также проверял многократно на тысячах и десятках тысяч)
# Я бы выбрал либо третий, либо второй вариант, склоняясь немного больше ко второму варианту.
# Потому что по скорости выполнения разницы практически нет, но они проще читаются.