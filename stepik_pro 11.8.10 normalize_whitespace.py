# Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна заменять все множественные пробелы в строке string на единственный пробел и возвращать полученный результат.

import re
def normalize_whitespace(string):
    result = re.sub(r'[ ]{2,}',r' ',string)
    return result


# Sample Input 1:
#
# print(normalize_whitespace('AAAA                A                AAAA'))
# Sample Output 1:
#
# AAAA A AAAA
# Sample Input 2:
#
# print(normalize_whitespace('Тут нет лишних пробелов'))
# Sample Output 2:
#
# Тут нет лишних пробелов
# Sample Input 3:
#
# print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))
# Sample Output 3:
#
# Тут н е т л и шних пробелов