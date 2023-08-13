# Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию,
# являются положительными целыми числами.
#
# Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
#
# TypeError, если аргумент не является целым числом
# ValueError, если аргумент является целым числом, но отрицательным или равным нулю
# Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим условиям или при наличии разных аргументов,
# несоответствующих разным условиям: TypeError, затем ValueError.
#
# Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.


def takes_positive(func):
    def wrapper(*args,**kwargs):
        for value in args + tuple(kwargs.values()):
            if not isinstance(value,int):
                raise TypeError
            if value <= 0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper




# SampleInput1:
#
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
# print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#
# SampleOutput1:
# 55
#
# SampleInput2:
#
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
# except Exception as err:
#     print(type(err))
# SampleOutput2:
#
# <class 'ValueError'>
#
#
# SampleInput3:
#
#
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum('10', 20, 10))
# except Exception as err:
#     print(type(err))
# SampleOutput3:
#
# <class 'TypeError'>

