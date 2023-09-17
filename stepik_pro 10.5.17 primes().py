# Функция primes()
# Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:
#
# left — натуральное число
# right — натуральное число
# Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно,
# а затем возбуждающий исключение StopIteration.
#
# Примечание 1. Гарантируется, что left <= right.
#
# Примечание 2. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя.
# Единица простым числом не является.

def primes(left,right):
    for i in range(left, right + 1):
        counter = 0
        for j in range(2, i + 1):
            if i % j == 0:
                counter += 1
        if counter == 1:
            yield i
    return 'stop'


# Sample Input 1:
#
# generator = primes(1, 15)
#
# print(*generator)
# Sample Output 1:
#
# 2 3 5 7 11 13
# Sample Input 2:
#
# generator = primes(6, 36)
#
# print(next(generator))
# print(next(generator))
# Sample Output 2:
#
# 7
# 11