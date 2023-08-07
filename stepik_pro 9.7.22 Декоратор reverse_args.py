# Декоратор reverse_args
# Реализуйте декоратор reverse_args, который передает все позиционные аргументы в декорируемую функцию func в обратном порядке.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

# SampleInput1:
# @reverse_args
# def power(a, n):
#     return a ** n
# print(power(2, 3))
# SampleOutput1:
# 9
#
# SampleInput2:
# @reverse_args
# def concat(a, b, c):
#     return a + b + c
# print(concat('apple', 'cherry', 'melon'))
# SampleOutput2:
#
# meloncherryapple


def reverse_args(func):
    def wrapper(*args,**kwargs):
        return func(*args[::-1],**kwargs)
    return wrapper



@reverse_args
def operation(a, b, name):
    return a // b + name
print(operation(10, 90, name=1))
#10