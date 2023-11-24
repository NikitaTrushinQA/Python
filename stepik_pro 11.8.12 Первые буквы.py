# Напишите программу, которая меняет местами первые две буквы в каждом слове, состоящем из двух или более букв.
#
# Формат входных данных
# На вход программе подается строка, содержащая слова.
#
# Формат выходных данных
# Программа должна в введенной строке заменить первые две буквы в каждом слове, состоящем из двух или более букв, и вывести полученный результат.
#
# Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W.

# Sample Input 1:
#
# This is Python
# Sample Output 1:
#
# hTis si yPthon
# Sample Input 2:
#
# Hi, everyone. Lets start a lesson!
# Sample Output 2:
#
# iH, veeryone. eLts tsart a elsson!
import re

def func(match_obj):
    s = match_obj.group(0)   # строка совпадения
    if len(s)>=2:
        return s[1]+s[0]+s[2:]
    else:
        return s

s = input()
result = re.sub(r'\w+',func,s)
print(result)