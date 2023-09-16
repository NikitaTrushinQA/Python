# Функция simple_sequence()
# Реализуйте генераторную функцию simple_sequence(), которая не принимает никаких аргументов.
#
# Функция должна возвращать генератор, порождающий бесконечную возрастающую последовательность натуральных чисел,
# в которой каждое число встречается столько раз, каково оно:
# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ..


def simple_sequence():
    n = 0
    while True:
        n += 1
        for i in range(n):
            yield n
