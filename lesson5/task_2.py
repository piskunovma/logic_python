# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

def sum_func16(digit1, digit2):
    dict_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13,
                'E': 14, 'F': 15}

    list_num = []
    for key, _ in dict_num.items():
        list_num.append(key)

    result = deque()
    discharge = 0

    if len(digit2) > len(digit1):
        digit1, digit2 = digit2, digit1

    while digit1:
        if digit2:
            number_res = dict_num[digit1.pop()] + dict_num[digit2.pop()] + discharge
        else:
            number_res = dict_num[digit1.pop()] + discharge

        if number_res < 16:
            discharge = 0
        else:
            discharge = 1
            number_res -= 16

        result.appendleft(list_num[number_res])

    if discharge == 1:
        result.appendleft('1')

    return list(result)

digit1 = list(input('Введите первое шестнадцатиричное число: ').upper())
digit2 = list(input('Введите второе шестнадцатиричное число: ').upper())

print(f'{digit1} + {digit2} = {sum_func16(digit1, digit2)}')