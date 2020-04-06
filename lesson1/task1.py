# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

user_number = int(input('Введите трехзначное число: '))

num1 = user_number // 100
num2 = user_number % 100 // 10
num3 = user_number % 10

sum_result = num1 + num2 + num3
prod_result = num1 * num2 * num3
print(f'Сумма - {sum_result}.\nПроизведение - {prod_result}.')