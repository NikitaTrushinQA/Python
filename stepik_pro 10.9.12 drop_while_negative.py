# Функция drop_while_negative()
# Реализуйте функцию drop_while_negative(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементами которого являются целые числа
# Функция должна возвращать итератор, генерирующий все числа итерируемого объекта iterable, начиная с первого неотрицательного числа.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

from itertools import dropwhile
def drop_while_negative(iterable):
    yield from  dropwhile(lambda x:x<0,iterable)

# Sample Input 1:
#
# numbers = [-3, -2, -1, 0, 1, 2, 3]
#
# print(*drop_while_negative(numbers))
# Sample Output 1:
#
# 0 1 2 3
# Sample Input 2:
#
# iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])
#
# print(*drop_while_negative(iterator))
# Sample Output 2:
#
# 0 1 2 3 -4 -5 -6
# Sample Input 3:
#
# iterator = iter([-3, -2, -1, -4, -5, -6])
#
# print(list(drop_while_negative(iterator)))
# Sample Output 3:
#
# []