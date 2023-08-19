
# Декоратор strip_range
# Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:
#
# start — неотрицательное целое число
# end — неотрицательное целое число
# char — одиночный символ, по умолчанию равный точке .
#
# Декоратор должен изменять возвращаемое значение декорируемой функции,
# заменяя все символы в диапазоне индексов от start (включительно) до end (не включительно) на символ char.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
#
# Примечание 2. Гарантируется, что start < end.
#
# Примечание 3. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.


import functools

def strip_range(start,end,char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            res =list(func(*args,**kwargs))
            try:
                for i in range(start,end):
                    res[i] = char
                result = ''.join(res)
            except:
                for j in range(start,len(res)):
                    res[j] = char
                result = ''.join(res)
            return result
        return wrapper
    return decorator


# SampleInput1:
#
# @strip_range(3, 5)
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
# SampleOutput1:
# bee..ek
#
# SampleInput2:
# @strip_range(3, 20, '_')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
# SampleOutput2:
# bee____
#
# SampleInput3:
#
# @strip_range(20, 30)
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())
# SampleOutput3:
#
# beegeek