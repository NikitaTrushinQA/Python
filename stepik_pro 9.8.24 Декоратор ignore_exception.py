# Реализуйте декоратор ignore_exception, который принимает произвольное количество позиционных аргументов — типов исключений, и выводит текст:
#
# Исключение <тип исключения> обработано
# если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.
#
# Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.


import functools

def ignore_exception(*exceptions):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                print(f"Исключение {e.__class__.__name__} обработано")
        return wrapper
    return decorator


# SampleInput1:
#
# @ignore_exception(ZeroDivisionError, TypeError, ValueError)
# def f(x):
#     return 1 / x
#
#
# f(0)
#
# SampleOutput1:
#
# Исключение
# ZeroDivisionError
# обработано
#
# SampleInput2:
#
# min = ignore_exception(ZeroDivisionError)(min)
#
# try:
#     print(min(1, '2', 3, [4, 5]))
# except Exception as e:
#     print(type(e))
# SampleOutput2:
#
# <
#
# class 'TypeError'>