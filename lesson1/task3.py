# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

user_number = int(input('Введите номер буквы в алфавите от 1 до 26: '))

result_number = chr(ord('a') + user_number - 1)

print('Это буква', result_number)