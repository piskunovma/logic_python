# Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы
# с наиболее эффективным использованием памяти.

import sys

# macOS Catalina 10.15.4, 64-разрядная. Версия интерпретатора - Python 3.7

# Функция подсчета затрачиваемой памяти
def size_func(obj):
    sum_memory = sys.getsizeof(obj)

    # print(f'type={type(obj)}, size={sys.getsizeof(obj)}, obj={obj}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                sum_memory += size_func(key)
                sum_memory += size_func(value)
        elif not isinstance(obj, str):
            for item in obj:
                if item is not True and item is not False:
                    sum_memory += size_func(item)
    return sum_memory


# Вариант первый:
def my_func(number):
    global i
    first_num = 2
    idx = 1

    while idx != number:
        first_num += 1

        for i in range(2, first_num):
            if first_num % i == 0:
                break

        else:
            idx += 1

    tuple_for_sum = ((i, number, idx, range(2, first_num), first_num))
    sum_res = size_func(tuple_for_sum)
    return f'Ваше простое число - {first_num}.\n' \
           f'Сумма памяти переменных - {sum_res - sys.getsizeof(tuple_for_sum)} байт.'

print(my_func(10))
print('*' * 50)

# Вариант второй:
def my_eratosphens(number):
    global idx, i
    CONST = 10
    array = [i for i in range(2, (number + 1) * CONST)]

    if number == 1:
        tuple_for_sum = (CONST, array, number)
        sum_res = size_func(tuple_for_sum)
        return f'Ваше простое число - {array[number - 1]} .\n' \
           f'Сумма памяти переменных - {sum_res - sys.getsizeof(tuple_for_sum) + sys.getsizeof(False)} байт.'

    p = 2
    while p < number:
        idx = 0
        for i in array:
            if i >= p ** 2:
                if i % p == 0:
                    array[idx] = False
            idx += 1
        p += 1
    result_list = [i for i in array if i != False]

    tuple_for_sum = (CONST, array, p, number, result_list, i, idx)
    sum_res = size_func(tuple_for_sum)
    return f'Ваше простое число - {result_list[number - 1]} .\n' \
           f'Сумма памяти переменных - {sum_res - sys.getsizeof(tuple_for_sum) + sys.getsizeof(False)} байт.'

print(my_eratosphens(4))
print('*' * 50)

# Вариант третий:
def eratosphen_teach(num):
    global item
    for_sum = 0
    CONST = 10
    array = [True for _ in range(num * CONST)]

    count = 0
    for i in range(2, len(array)):

        if array[i]:

            count += 1
            if count == num:

                tuple_for_sum = (CONST, array, count, i, item)
                sum_res = size_func(tuple_for_sum) + for_sum

                return f'Ваше простое число - {i} .\n' \
                       f'Сумма памяти переменных - {sum_res - sys.getsizeof(tuple_for_sum) + sys.getsizeof(False) + sys.getsizeof(True)} байт.'
                # return i

            for item in range(i ** 2, len(array), i):
                array[item] = False

print(eratosphen_teach(8))

# Вывод: В плане затрачиваемой памяти наиболее менее затратный  - первый вариант.
# Но он также является наиболее долгим на больших значениях.
# Я бы выбрал 3ий вариант, он менее затратен по памяти чем второй вариант,
# но по скорости работы и удобству чтения кода сильно превосходит остальные варианты.

# Так же не сломался вывод первого простого числа во всех вариантах.
# (Во втором вроде поправил, отдельно добавив обработку случая когда ищем первое простое число.
# В первом можно сделать также, но не уверен, что это в принципе верное решение, поэтому там не стал ничего менять.)
# Почему так произошло полноценного понимания нет, буду рад любым комментариям, которые помогут разобраться.
# Как я понял, это из-за того, что при поиске первого простого числа,
# некоторые переменные в коде не определяются и как следствие не выводятся и не суммируются позже