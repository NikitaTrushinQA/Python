# Реализуйте декоратор add_attrs, который принимает произвольное количество именованных аргументов и устанавливает их в качестве атрибутов декорируемой функции.
# Названием атрибута должно являться имя аргумента, значением атрибута — значение аргумента.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.

import functools
def add_attrs(**attrs):
    def decorator(func):
        for key,value in attrs.items():
            func.__dict__[key] = value
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            return func(*args,**kwargs)
        return wrapper
    return decorator


# SampleInput1:
#
# @add_attrs(attr1='bee', attr2='geek')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)
#
# SampleOutput1:
#
# bee
# geek
#
# SampleInput2:
#
#
# @add_attrs(attr2='geek')
# @add_attrs(attr1='bee')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)
# print(beegeek.__name__)
#
# SampleOutput2:
# bee
# geek
# beegeek
