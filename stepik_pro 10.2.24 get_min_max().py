# Функция get_min_max()
# Реализуйте функцию get_min_max(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементы которого сравнимы между собой
# Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент итерируемого объекта iterable,
# вторым — максимальный элемент итерируемого объекта iterable.
# Если итерируемый объект iterable пуст, функция должна вернуть значение None.

import copy

def get_min_max(iterable):
    try:
        copy_iterable = copy.copy(iterable)
        result=(min(iterable),max(copy_iterable))
        return result
    except:
        return None

# Sample Input 1:
#
# iterable = iter(range(10))
#
# print(get_min_max(iterable))
# Sample Output 1:
#
# (0, 9)
# Sample Input 2:
#
# iterable = [6, 4, 2, 33, 19, 1]
#
# print(get_min_max(iterable))
# Sample Output 2:
#
# (1, 33)
# Sample Input 3:
#
# iterable = iter([])
#
# print(get_min_max(iterable))
# Sample Output 3:
#
# None