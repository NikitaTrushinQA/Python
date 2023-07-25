# Рассмотрим семейство функций — квадратных трехчленов. Все эти функции имеют один и тот же вид:
# f(x)=a*x**2 + b*x + c
#
# Реализуйте функцию generator_square_polynom(), которая принимает три аргумента в следующем порядке:
# a — вещественное число, коэффициент a
# b — вещественное число, коэффициент b
# c — вещественное число, коэффициент c
#
# Функция generator_square_polynom() должна возвращать функцию, которая принимает в качестве аргумента вещественное число x
# и возвращает значение выражения a*x**2 + b*x + c
#
# Примечание 1. Рассмотрим пример из первого теста. Вызов generator_square_polynom(1, 2, 1) возвращает функцию,
# соответствующую квадратному трехчлену x**2 + 2*x + 1. Функция присваивается переменной f.
# Далее полученная функция вызывается с аргументом 5 и возвращает значение 5**2 +5*2+1-36.
#
# Sample Input 1:
# f = generator_square_polynom(1, 2, 1)
# print(f(5))
# Sample Output 1:
# 36
#
# Sample Input 2:
# print(generator_square_polynom(9, 52, 64)(8))
# Sample Output 2:
# 1056
#
# Sample Input 3:
# f = generator_square_polynom(26, 83, 22)
# print(f(55))
# Sample Output 3:
# 83237

def generator_square_polynom(a,b,c):
    def foo(x):
        f = a*x**2 + b*x + c
        return f
    return foo

f = generator_square_polynom(26, 83, 22)
print(f(55))