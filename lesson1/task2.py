# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

user_letter1 = ord(input('Введите первую букву латинского алфавита: '))
user_letter2 = ord(input('Введите вторую букву латинского алфавита: '))

letter1 = user_letter1 - ord('a') + 1
letter2 = user_letter2 - ord('a') + 1
between_letter = abs(user_letter1 - user_letter2) - 1

print('Первая буква находится на ', letter1, 'месте в алфавите.\nВторая буква находится на', letter2, 'месте в алфавите.')
print('Букв между -', between_letter)