# Точка с запятой
# Напишите программу, которая разбивает строку по символам точки, запятой и точки с запятой.
#
# Формат входных данных
# На вход программе подается строка, содержащая различные значения,
# разделенные символами точки ., запятой ,или точки с запятой ;, вокруг которых могут располагаться пробелы.
#
# Формат выходных данных
# Программа должна разбить введенную строку по символам точки, запятой и точки с запятой, захватывая вокруг стоящие пробелы,
# и вывести все значения, полученные при разбиении, через пробел.

import re

s = input()

result = re.split(r'\s*[,;.]\s*',s)
print(*result)


# Sample Input 1:
# bee,geek . Python   ,  C++

# Sample Output 1:
#
# bee geek Python C++
# Sample Input 2:
#
# py py; hi  hi; go-go-go
# Sample Output 2:
#
# py py hi  hi go-go-go
# Sample Input 3:
#
# arthur;timur,dima.anri
# Sample Output 3:
#
# arthur timur dima anri