# 1.
# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

print('Введите любое число: ', end='')
flt = input()
in_str = flt.split('.')
print(f'Для введенного числа {flt} сумма всех чисел равна:', end=' ')
flt = float(flt)
flt = abs(flt)
sUm = 0

while flt != int(flt):
    flt *= 10
    flt = round(flt, len(in_str[1][:]))     # паразит, добавляет ничтожную величину - ракета падает
flt = int(flt)

while flt != 0:
    sUm += flt % 10
    flt //= 10

print(sUm)
