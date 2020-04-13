# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

user_number = int(input('Введите целое натуральное число: '))
my_number = user_number

res1 = 0
res2 = 0

while user_number > 0:
    if user_number % 2 == 0:
        res1 += 1

    else:
        res2 += 1
    user_number = user_number // 10

print(f"В числе {my_number} четных чисел - {res1}, а нечетных чисел - {res2}.")