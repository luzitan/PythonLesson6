"""
Задача 1: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""

# a1 = int(input("Введите первый элемент арифметической прогрессии: "))
# d = int(input("Введите разность арифметической прогрессии: "))
# n = int(input("Введите количество элементов арифметической прогрессии: "))
# arifmet = [a1]
#
# for i in range(2, n+1):
#     arifmet.append(a1 + (i-1)*d)
# print(arifmet)


"""
Задача 2: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
"""

sp = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = 5
max = 10
index = []

for i in range(len(sp)):
    if min <= sp[i] <= max:
        index.append(i)
print(index)
