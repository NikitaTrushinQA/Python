# Функция take()
# Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность из первых n элементов итерируемого объекта iterable.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

from itertools import compress
def take(iterable,n):
    result = compress(iterable,[True for i in range(n)])
    yield from result


# Sample Input 1:
#
# print(*take(range(10), 5))
# Sample Output 1:
#
# 0 1 2 3 4
# Sample Input 2:
#
# iterator = iter('beegeek')
#
# print(*take(iterator, 22))
# Sample Output 2:
#
# b e e g e e k
# Sample Input 3:
#
# iterator = iter('beegeek')
#
# print(*take(iterator, 1))
# Sample Output 3:
#
# b