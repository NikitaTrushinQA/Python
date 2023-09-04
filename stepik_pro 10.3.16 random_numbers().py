# Функция random_numbers()
# Реализуйте функцию random_numbers(), которая принимает два аргумента:
#
# left — целое число
# right — целое число
# Функция должна возвращать итератор, генерирующий бесконечную последовательность случайных целых чисел в диапазоне от left до right включительно.
#
# Примечание 1. Гарантируется, что left <= right.


import random
def random_numbers(left,right):
    values = iter(lambda:random.randint(left,right), left-1)
    it = iter(values)
    return it


# Sample Input 1:
#
# iterator = random_numbers(1, 1)
#
# print(next(iterator))
# print(next(iterator))
# Sample Output 1:
#
# 1
# 1
# Sample Input 2:
#
# iterator = random_numbers(1, 10)
#
# print(next(iterator) in range(1, 11))
# print(next(iterator) in range(1, 11))
# print(next(iterator) in range(1, 11))
# Sample Output 2:
#
# True
# True
# True