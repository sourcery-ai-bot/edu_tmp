# -*- coding: utf-8 -*-

__author__ = 'gkitg'


''' 
1 задача:
Ваня набрал несколько операций в интерпретаторе и получал результаты:
Код: a == a**2, Результат: True
Код: a == a*2, Результат: True
Код: a > 999999, Результат: True
Вопрос: Чему была равна переменная a, если точно известно, что её значение не изменялось?
'''

a = float('inf')


'''
2 задача: 
Дано произвольное целое число, вывести самую большую цифру этого числа.
Например, дается x = 58375.
Нужно вывести максимальную цифру в данном числе, т.е. 8.
Подразумевается, что мы не знаем это число заранее.
Число приходит в виде целого беззнакового.
'''

x = int(input())
a = x % 10
x //= 10
while x > 0:
    if x % 10 > a:
        a = x % 10
    x //= 10
print(a)


'''
3 задача:
Исходные значения двух переменных запросить у пользователя.
Поменять значения переменных местами. Вывести новые значения на экран.
Решите задачу, используя только две переменные.
'''

x = int(input())
y = int(input())
print('x =', x,'| ' 'y =', y)
x, y = y, x
print('x =', x,'| ' 'y =', y)


# Запросить число у пользователя и развернуть обратно по порядку.
# Пример, если число 7089, вывести число 9807.

x = int(input())
a = 0
while x > 0:
    a = a * 10 + x % 10
    x //= 10
print(a)


'''
4 задача:
Программа, вычисляющая корни квадратного уравнения вида
ax² + bx + c = 0
Коэффициенты уравнения вводятся пользователем.
'''

import math

print('Вычисляет корни квадратного уравнения вида ax² + bx + c = 0')

a = float(input('Введите значение A: '))
b = float(input('Введите значение B: '))
c = float(input('Введите значение C: '))

discriminant = b**2 - 4 * a * c
print('Дискриминант D = %.2f' % discriminant)

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print('x1 = %.2f \nx2 = %.2f' % (x1, x2))
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = %.2f' % x)
else:
    print('корней нет')


# 5 задача
# Вывести цифры по одной, в обратном порядке

def turn(x):
    if x > 0:
        print(x % 10)
        turn(x // 10)

turn(9876543210)