# 3.
# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

import random
lEn = 0
listN = []
while lEn < 2 or 15 < lEn:
    print('Задайте длину списка от 2 до 15: ', end='')
    lEn = int(input())

element = None
for i in range(lEn):
    print(f'Введите {i}-й элемент списка:', end=' ')
    element = input()
    listN.append(element)
print('Ваш список:')
print(*listN, sep='   ')

listTemp = []
rndm = None
for j in range(lEn):
    for i in range(lEn):
        if len(listN) > 1:
            rndm = random.randint(0, len(listN))
            if len(listN) == rndm:
                rndm -= 1
        else:
            rndm = 0
        listTemp.append(listN[rndm])
        del listN[rndm]
    listN = listTemp
    listTemp = []
    print('Перемешанный список:')
    print(*listN, sep='   ')