# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# вариант 1
num = int(input('Введите целое число: '))
even, odd = 0, 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num //= 10
print(f"четных - {even}, нечетных - {odd}")


# вариант 2
num = input('Введите целое число: ')
even = odd = 0
for i in num:
    if i in {'0', '2', '4', '6', '8'}:
        even += 1
    else:
        odd += 1
print(f"четных - {even}, нечетных - {odd}")