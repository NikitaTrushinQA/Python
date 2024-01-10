# Функция is_decimal()
# Будем считать вещественным числом последовательность из одной или более цифр,
# которая может начинаться с необязательного символа дефиса -, а также содержать на любой позиции одну десятичную точку .
# , кроме случая, когда точка стоит перед символом дефиса.
#
# Реализуйте функцию is_decimal(), которая принимает один аргумент:
#
# string — строка, содержащая произвольный набор символов
# Функция должна возвращать True, если строка string представляет собой целое или вещественное число, или False в противном случае.

def is_decimal(string):
    try:
        result = float(string)
        return True
    except:
        return False

# Sample Input 1:
#
# print(is_decimal('100'))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# print(is_decimal('199.1'))
# Sample Output 2:
#
# True
# Sample Input 3:
#
# print(is_decimal('-0.2'))
# Sample Output 3:
#
# True