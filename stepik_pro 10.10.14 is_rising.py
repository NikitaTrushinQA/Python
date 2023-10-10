#   Функция is_rising()
# Реализуйте функцию is_rising(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементами которого являются числа
# Функция должна возвращать True, если элементы итерируемого объекта расположены строго по возрастанию, или False в противном случае.
#
# Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством, а также содержит не менее двух элементов.

from itertools import pairwise

def is_rising(iterable):

    result = all(map(lambda x: x[0]<x[1],pairwise(iterable)))
    return result


# Sample Input 1:

# print(is_rising([1, 2, 3, 4, 5]))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# iterator = iter([1, 1, 1, 2, 3, 4])
#
# print(is_rising(iterator))
# Sample Output 2:
#
# False
# Sample Input 3:
#
# iterator = iter(list(range(100, 200)))
#
# print(is_rising(iterator))
# Sample Output 3:
#
# True