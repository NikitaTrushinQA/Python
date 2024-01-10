# Функция is_fraction()
# Будем считать обыкновенной дробью последовательность из одной или более цифр, за которой следует прямая косая черта /,
# а затем — последовательность из одной или более цифр, хотя бы одна из которых отлична от нуля (знаменатель не может равняться нулю).
# Последовательность, представляющая собой обыкновенную дробь, может начинаться с необязательного символа дефиса -.
#
# Реализуйте функцию is_fraction(), которая принимает один аргумент:
#
# string — строка, содержащая произвольный набор символов
# Функция должна возвращать True, если строка string представляет собой обыкновенную дробь, или False в противном случае.

from fractions import Fraction

def is_fraction(string):
    if '/' not in string:
        return False
    else:
        try:
            result = Fraction(string)
            return True
        except:
            return False

# Sample Input 1:
#
# print(is_fraction('1000/1'))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# print(is_fraction('-54/9'))
# Sample Output 2:
#
# True
# Sample Input 3:
#
# print(is_fraction('71'))
# Sample Output 3:
#
# False