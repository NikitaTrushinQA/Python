
# Реализуйте декоратор retry, который принимает один аргумент:
#
# times — натуральное число
# Декоратор должен выполнять повторную попытку вызова декорируемой функции, если во время ее выполнения возникает ошибка.
# Декоратор должен вызывать ее до тех пор, пока не исчерпает количество попыток times, после чего должен возбуждать исключение MaxRetriesException.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции

class MaxRetriesException(Exception):
    pass


import functools
def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            nonlocal times
            while times:
                try:
                    return func(*args, **kwargs)
                except:
                    times -= 1
            raise MaxRetriesException
        return wrapper
    return decorator


# SampleInput1:
#
# @retry(3)
# def no_way():
#     raise ValueError
#
#
# try:
#     no_way()
# except Exception as e:
#     print(type(e))
# SampleOutput1:
#
# <class '__main__.MaxRetriesException'>
#
# 
# SampleInput2:
#
#
# @retry(8)
# def beegeek():
#     beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
#     if beegeek.calls < 5:
#         raise ValueError
#     print('beegeek')
#
#
# beegeek()
# SampleOutput2:
#
# beegeek