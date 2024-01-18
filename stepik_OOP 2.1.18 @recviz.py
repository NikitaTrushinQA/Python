# Декоратор @recviz
#
# Реализуйте декоратор @recviz, который полностью визуализирует выполнение декорируемой функции,
# в том числе и рекурсивной.
# Декоратор должен отображать все рекурсивные вызовы и возвращаемые значения, полученные при этих вызовах, причем рекурсивные вызовы,
# выполняемые в глубину, должны отделяться друг от друга четырьмя пробелами.
#
# Очередной вызов декорируемой функции при визуализации должен включать в себя знак ->, имя декорируемой функции и аргументы, переданные при этом вызове.
# Возвращаемое значение при визуализации должно включать в себя знак <- и непосредственно само возвращаемое значение.
#
# Примечание 1. Рекурсивный вызов и возвращаемое значение, полученное при этом вызове, должны находиться на одном уровне отступов.
#
# Примечание 2. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.


import functools


def recviz(func):
    func.level = -1

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func.level += 1  # либо можно nonlocal level

        pos_args = list(map(repr, args))
        keyword_args = [f'{k}={repr(v)}' for k, v in kwargs.items()]

        print('    ' * func.level + '->', f'{func.__name__}({", ".join(pos_args + keyword_args)})')
        value = func(*args, **kwargs)
        print('    ' * func.level + '<-', repr(value))
        func.level -= 1

        return value

    return wrapper


# Sample Input 1:
#
# @recviz
# def add(a, b):
#     return a + b
#
#
# add(1, b=2)
#
# Sample Output 1:
#
# -> add(1, b=2)
# < - 3
#
# Sample Input 2:
#
#
# @recviz
# def add(a, b, c, d, e):
#     return (a + b + c) * (d + e)
#
#
# add('a', b='b', c='c', d=3, e=True)
#
# Sample Output 2:
#
# -> add('a', b='b', c='c', d=3, e=True)
# < - 'abcabcabcabc'
#
# Sample Input 3:
#
#
# @recviz
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# fib(4)
#
# Sample Output 3:
#
# -> fib(4)
#     -> fib(3)
#         -> fib(2)
#         < - 1
#         -> fib(1)
#         < - 1
#     < - 2
#     -> fib(2)
#     < - 1
# < - 3