# Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая принимает два аргумента в следующем порядке:
#
# numbers — список целых или вещественных чисел
# step — целое число
# Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов, и возвращать значение None.
# Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.
#
# Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing.
# Также используйте нотацию |, а не тип Union из модуля typing.

# Sample Input 1:
#
# numbers = [1, 2, 3, 4, 5]
# cyclic_shift(numbers, 1)
#
# print(numbers)
# Sample Output 1:
#
# [5, 1, 2, 3, 4]
# Sample Input 2:
#
# numbers = [1, 2, 3, 4, 5]
# cyclic_shift(numbers, -2)
#
# print(numbers)
# Sample Output 2:
#
# [3, 4, 5, 1, 2]

from collections import deque
def cyclic_shift(numbers:list[int|float],step:int)->None:
    new_num = deque(numbers)
    new_num.rotate(step)
    numbers[:] = list(new_num)

