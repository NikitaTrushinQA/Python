# Ключевые слова
# В Python существуют ключевые слова, которые нельзя использовать для названия переменных, функций и классов. Для получения списка всех ключевых слов можно воспользоваться атрибутом kwlist из модуля keyword.
#
# Приведенный ниже код:
#
# import keyword
#
# print(keyword.kwlist)
# выводит:
#
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
#  'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.
#
# Формат входных данных
# На вход программе подается строка.
#
# Формат выходных данных
# Программа должна в введенном тексте заменить все ключевые слова (в любом регистре) на строку <kw> и вывести полученный результат.
# Sample Input 1:
#
# True, assert, as, false, or, Import
# Sample Output 1:
#
# <kw>, <kw>, <kw>, <kw>, <kw>, <kw>
# Sample Input 2:
#
# True or False - that's the question
# Sample Output 2:
#
# <kw> <kw> <kw> - that's the question
# Sample Input 3:
#
# True and False - that is the question
# Sample Output 3:
#
# <kw> <kw> <kw> - that <kw> the question

import keyword
import re


def func(match_obj):
    s = match_obj.group(0)   # строка совпадения
    if s.upper() in list(map(lambda x:x.upper(),keyword.kwlist)):
        return '<kw>'
    else:
        return s


s = input()
result = re.sub(r'\w+',func,s)
print(result)

