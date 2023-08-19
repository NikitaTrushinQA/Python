# Реализуйте декоратор returns, который принимает один аргумент:
#
# datatype — тип данных
# Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype.
# Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

import functools

def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            res = func(*args,**kwargs)
            if not isinstance(res,datatype):
                raise TypeError
            return res
        return wrapper
    return decorator


# Sample Input 1:
#
# @returns(int)
# def add(a, b):
#     return a + b
#
# print(add(10, 5))
# Sample Output 1:
#
# 15
# Sample Input 2:
#
# @returns(int)
# def add(a, b):
#     return a + b
#
# try:
#     print(add('199', '1'))
# except TypeError as e:
#     print(type(e))
# Sample Output 2:
#
# <class 'TypeError'>