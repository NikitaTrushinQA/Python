# Аббревиатура — слово, образованное сокращением слова или словосочетания и читаемое по алфавитному названию начальных букв или по начальным звукам слов,
# входящих в него.
#
# Реализуйте функцию abbreviate(), которая принимает один аргумент:
#
# phrase — фраза
# Функция должна создавать из фразы phrase аббревиатуру в верхнем регистре и возвращать её.
#
# Примечание 1. В аббревиатуре должны присутствовать как начальные буквы слов,
# так и начальные буквы подслов, начинающихся с заглавной буквы, например, JavaScript Object Notation -> JSON.

import re

def abbreviate(phrase):
    result = re.findall(r'\b\w|\B[A-Z]',phrase)
    return ''.join(result).upper()



# Sample Input 1:
#
# print(abbreviate('javaScript object notation'))
# Sample Output 1:
#
# JSON
# Sample Input 2:
#
# print(abbreviate('frequently asked questions'))
# Sample Output 2:
#
# FAQ
# Sample Input 3:
#
# print(abbreviate('JS game sec'))
# Sample Output 3:
#
# JSGS