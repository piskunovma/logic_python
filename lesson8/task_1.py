# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

import hashlib


def my_func_hash(value):

    value = str(value)

    length = len(value)

    set_for_hash = set()

    idx = 0
    while idx != length:
        if idx == 0:
            for j in range(1, length):
                my_hash = hashlib.sha1(value[idx:j].encode('utf-8')).hexdigest()
                # print(value[idx:j])
                set_for_hash.add(my_hash)
        else:
            for j in range(idx + 1, length + 1):
                my_hash = hashlib.sha1(value[idx:j].encode('utf-8')).hexdigest()
                # print(value[idx:j])
                set_for_hash.add(my_hash)
        idx += 1

    return len(set_for_hash)


# my_string = input('Введите строку: ')
my_string = 'sova'

print(f'Количество подстрок в строке "{my_string}": {my_func_hash(my_string)}')