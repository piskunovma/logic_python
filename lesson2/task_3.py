# 3. Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

user_number = int(input('Введите целое число: '))
my_number = user_number

res_num = 0
while user_number > 0:
    res_num = res_num * 10 + user_number % 10
    user_number = user_number // 10

print(f"Число обратное числу '{my_number}' - {res_num}.")