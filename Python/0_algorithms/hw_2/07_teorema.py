# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def sum_natural(n):
    assert n < 999, 'Слишком большое число'
    return n if n == 1 else n + sum_natural(n - 1)


n = int(input('Введите любое натуральное число: '))

left = sum_natural(n)
right = n * (n + 1) // 2

print(f'left = {left}')
print(right)
print(left == right)