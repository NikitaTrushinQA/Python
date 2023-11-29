# Сумма чисел
# Напишите программу, которая складывает все натуральные числа в строке, находящиеся в указанном диапазоне индексов.
#
# Формат входных данных
# На вход программе сначала подаются два целых числа a и b, больших или равных 0, разделенные пробелом, а затем — строка.
#
# Формат выходных данных
# Программа должна вывести сумму всех натуральных чисел в введенной строке,
# находящихся в диапазоне индексов от a (включительно) до b (не включительно).
# Если в указанном диапазоне нет ни одного числа, программа должна вывести 0.

import re

a,b = map(int,input().split(' '))
string = input()
regex_obj = re.compile(r'\d+')
result = sum(map(int,regex_obj.findall(string,pos=a,endpos=b)))
print(result)


# Sample Input 1:
#
# 0 5
# 11:20 a.m. - 12:00 p.m
# Sample Output 1:
#
# 31
# Sample Input 2:
#
# 0 10
# Нет ни одного числа в этой строке
# Sample Output 2:
#
# 0
# Sample Input 3:
#
# 0 100
# Нет ни одного числа в этой строке
# Sample Output 3:
#
# 0