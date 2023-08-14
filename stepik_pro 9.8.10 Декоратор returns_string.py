# Реализуйте декоратор returns_string, который проверяет, что возвращаемое значение декорируемой функции принадлежит типу str.
# Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

import functools
def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if not isinstance(func(*args,**kwargs),str):
            raise TypeError
        return func(*args,**kwargs)
    return wrapper


# SampleInput1:
#
#
# @returns_string
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
# SampleOutput1:
#
# beegeek
# SampleInput2:
#
#
# @returns_string
# def add(a, b):
#     return a + b
#
#
# try:
#     print(add(3, 7))
# except TypeError as e:
#     print(type(e))
# SampleOutput2:
#
# <class 'TypeError'>