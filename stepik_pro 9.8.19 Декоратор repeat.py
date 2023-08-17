# Реализуйте декоратор repeat, который принимает один аргумент:
#
# times — натуральное число
# Декоратор должен вызывать декорируемую функцию times раз.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.



import functools
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(1,times+1):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator


# SampleInput1:
# @repeat(3)
# def say_beegeek():
#     '''documentation'''
#     print('beegeek')
#
# say_beegeek()
# SampleOutput1:
#
# beegeek
# beegeek
# beegeek
#
# SampleInput2:
#
# @repeat(4)
# def say_beegeek():
#     '''documentation'''
#     print('beegeek')
#
#
# print(say_beegeek.__name__)
# print(say_beegeek.__doc__)
#
# SampleOutput2:
# say_beegeek
# documentation