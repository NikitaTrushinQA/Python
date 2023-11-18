# Напишите программу, определяющую:
#
# количество строк, в которых bee встречается в качестве подстроки не менее двух раз
# количество строк, в которых geek встречается в качестве слова хотя бы один раз
#
# Формат входных данных
# На вход программе произвольное количество строк, каждая из которых содержит набор произвольных символов.
#
# Формат выходных данных
# Программа должна вывести два числа:
#
# первое — количество строк, в которых bee встречается в качестве подстроки не менее двух раз
# второе — количество строк, в которых geek встречается в качестве слова хотя бы один раз
#
# каждое на отдельной строке.
#
# Примечание 1. Словом будем считать любую непрерывную последовательность из одного или нескольких символов, соответствующих \w.
#
# Примечание 2. Строка может одновременно удовлетворять обоим условиям.

import re
import sys

patt1 = r'.*bee.*bee.*'
patt2 = r'\bgeek\b'
counter1 = 0
counter2 = 0
for word in sys.stdin:
    if re.search(patt1,word.strip()):
        counter1+=1
    if re.search(patt2,word.strip()):
        counter2+=1
print(counter1)
print(counter2)

# Sample Input 1:
#
# beebee bee
# beegeek
# bee geek bee
# Sample Output 1:
#
# 2
# 1
# Sample Input 2:
#
# abigail alex
# clint dwarf
# emily
# gil
# Sample Output 2:
#
# 0
# 0