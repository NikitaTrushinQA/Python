#Сумма дробей 2
#На вход программе подается натуральное число n.
#Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения
#1/1!+1/2!+1/3!+1/n!
#Формат входных данных
#На вход программе подается натуральное число nn.

#Формат выходных данных
#Программа должна вывести ответ на задачу.

#Примечание 1. Результирующая дробь должна быть несократимой.

#Примечание 2. Для вычисления факториала можно использовать функцию factorial из модуля math.
from fractions import Fraction as F
from math import*
n = int(input())
result = 0
for i in range(1,n+1):
    result+=F(1,factorial(i))
print(F(result))