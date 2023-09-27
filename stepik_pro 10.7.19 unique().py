# функция unique()
# Реализуйте генераторную функцию, которая принимает один аргумент:
#
# iterable — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable без дубликатов.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

from collections import Counter
def unique(iterable):
    result = Counter(iterable)
    yield from (i for i in result)


# Sample Input 1:
#
# numbers = [1, 2, 2, 3, 4, 5, 5, 5]
#
# print(*unique(numbers))
# Sample Output 1:
#
# 1 2 3 4 5
# Sample Input 2:
#
# iterator = iter('111222333')
# uniques = unique(iterator)
#
# print(next(uniques))
# print(next(uniques))
# print(next(uniques))
# Sample Output 2:
#
# 1
# 2
# 3