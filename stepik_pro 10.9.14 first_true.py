# функция first_true()
# Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
# Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция predicate вернула значение True.
# Если такого элемента нет, функция first_true() должна вернуть значение None.
#
# Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве аргумента значения.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.


def first_true(iterable,predicate):
    result = filter(predicate,iterable)
    return  next(result,None)



# Sample Input 1:
#
# numbers = [1, 1, 1, 1, 2, 4, 5, 6]
#
# print(first_true(numbers, lambda num: num % 2 == 0))
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
#
# print(first_true(numbers, lambda num: num > 10))
# Sample Output 2:
#
# 100
# Sample Input 3:
#
# numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
#
# print(first_true(numbers, None))
# Sample Output 3:
#
# 69