# цикл вместо дублирования 4 строчек кода
from collections import namedtuple

all_comp = []
Comp = namedtuple('Comp', 'name, p1, p2, p3, p4, total')
num = int(input('num = '))
for _ in range(num):
    name = input('name = ')
    spam = [int(input(f'{j} = ')) for j in range(1, 5)]
    all_comp.append(Comp(name, *spam, sum(spam)))

print(all_comp)

""" пример работы звёздочки """
lst = [2, 4, 6]
print(lst)
print(*lst)
for i in lst:
    print(i, end=' ')
