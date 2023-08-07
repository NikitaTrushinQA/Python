# Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

# SampleInput 1
# @do_twice
# def beegeek():
#     print('beegeek')
#
# beegeek()
# SampleOutput1:
# beegeek
# beegeek
#
# SampleInput2:
# @do_twice
# def beegeek():
#     print('beegeek')
# print(beegeek())
# SampleOutput2:
# beegeek
# beegeek
# None

def do_twice(func):
    def wrapper(*args,**kwargs):
        func(*args, **kwargs)
        m = func(*args, **kwargs)
        return m
    return wrapper



@do_twice
def beegeek():
    print('beegeek')
beegeek()