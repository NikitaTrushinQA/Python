# Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию, являются положительными целыми числами.
#
# Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
#
# TypeError, если аргумент не является целым числом
# ValueError, если аргумент является целым числом, но отрицательным или равным нулю
# Примечание 1.
# Приоритет возбуждения исключений при несоответствии аргумента обоим условиям или при наличии разных аргументов,
# несоответствующих разным условиям: TypeError, затем ValueError.

# Sample Input 1:
#
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
# print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#
# SampleOutput 1:
# 55
#
# Sample Input 2:
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
# Sample Output 2:
#
# <class 'ValueError'>

def takes_positive(func):
    def wrapper(*args,**kwargs):
        for value in args + tuple(kwargs.values()):
            if not isinstance(value,int):
                raise TypeError
            if value <= 0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper
