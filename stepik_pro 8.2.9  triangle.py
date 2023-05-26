# Реализуйте функцию triangle() с использованием рекурсии, которая принимает один аргумент:
#
# h — натуральное число
# Функция должна выводить звездный треугольник с высотой h в соответствии со следующим примером:
#
# ...
# *****
# ****
# ***
# **
# *
#
# Sample Input 1:
#
# triangle(3)
# Sample Output 1:
#
# ***
# **
# *
# Sample Input 2:
#
# triangle(5)
# Sample Output 2:
#
# *****
# ****
# ***
# **
# *

def triangle(h):
    while h>0:
        print('*'*h)
        return triangle(h-1)