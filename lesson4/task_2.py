# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход
# натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

import cProfile


# Вариант без использования "Решета Эратосфена"
def my_func(number):
    first_num = 2
    idx = 1
    while idx != number:
        first_num += 1
        for i in range(2, first_num):
            if first_num % i == 0:
                break
        else:
            idx += 1
    # print(first_num)
    return first_num


my_func(57)

cProfile.run('my_func(10)') # 0.000
cProfile.run('my_func(100)') # 0.002
cProfile.run('my_func(1000)') # 0.296
cProfile.run('my_func(2000)') # 1.272
cProfile.run('my_func(10000)') # 38.246




