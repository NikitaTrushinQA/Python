# Слова
# Напишите программу, которая принимает на вход строку текста и некоторое слово и определяет, сколько вхождений данного слова содержится в введенном тексте.
#
# Формат входных данных
# На вход программе на первой строке подается текст, на второй — слово.
#
# Формат выходных данных
# Программа должна определить, сколько вхождений данного слова содержится в веденном тексте, и вывести полученный результат.
#
# Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W.

import re
text, word = input(),input()

result = len(re.findall(fr'\b{word}\b',text))
print(result)


# Sample Input 1:
#
# foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo.
# foo
# Sample Output 1:
#
# 6
# Sample Input 2:
#
# Sunday, Monday, Tuesday, Wednesday
# day
# Sample Output 2:
#
# 0
# Sample Input 3:
#
# Hhelo Hey Human hacker
# H
# Sample Output 3:
#
# 0