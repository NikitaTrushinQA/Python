# Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:
#
# number — неотрицательное целое число
# Функция должна возвращать строковое представление числа number в двоичной системе счисления.

# Sample Input 1:
# print(to_binary(15))
# Sample Output 1:
# 1111
#
# Sample Input 2:
# print(to_binary(0))
# Sample Output 2:
# 0
#
# Sample Input 3:
# print(to_binary(1))
# Sample Output 3:
# 1

def to_binary(number):
    if number <= 1:
        return str(number)
    else:
        return to_binary(number // 2) + str(number % 2)