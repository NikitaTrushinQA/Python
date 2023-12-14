# Функция is_integer()
#
# Целым числом будем считать последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -.
#
# Реализуйте функцию is_integer(), которая принимает один аргумент:
#
# string — строка, содержащая произвольный набор символов
# Функция должна возвращать True, если строка string представляет собой целое число, или False в противном случае.

def is_integer(string):
    try:
        result = int(string)
        return True
    except:
        return False


# Sample Input 1:
#
# print(is_integer('199'))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# print(is_integer('-43'))
# Sample Output 2:
#
# True
# Sample Input 3:
#
# print(is_integer('5f'))
# Sample Output 3:
#
# False
# Sample Input 4:
#
# print(is_integer('5.0'))
# Sample Output 4:
#
# False
# Sample Input 5:
#
# print(is_integer('1.1'))
# Sample Output 5:
#
# False