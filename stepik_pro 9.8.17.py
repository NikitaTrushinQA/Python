# Декоратор prefix
# Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:
#
# string — произвольная строка
# to_the_end — булево значение, по умолчанию равное False
# Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции.
# Если to_the_end имеет значение True,строка string добавляется в конец, если False — в начало.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
#
# Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.


import functools
def prefix(string,to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            if to_the_end:
                result = func(*args,**kwargs)+string
            else:
                result = string + func(*args,**kwargs)
            return result
        return wrapper
    return decorator


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'


print(get_bonus())



# SampleInput1:
# @prefix('€')
# def get_bonus():
#     return '2000'
#
# print(get_bonus())
# SampleOutput1:
# €2000
#
# SampleInput2:
# @prefix('$$$', to_the_end=True)
# def get_bonus():
#     return '2000'
#
# print(get_bonus())
# SampleOutput2:
# 2000$$$