# Функция multiple_split()
# Реализуйте функцию multiple_split(), которая принимает два аргумента:
#
# string — строка
# delimiters — список строк

# Функция должна разбивать строку string на подстроки, используя в качестве разделителей строки из списка delimiters,
# и возвращать полученный результат в виде списка.
#
# Примечание 1. Другими словами, функция multiple_split() должна работать аналогично строковому методу split(),
# за тем исключением, что delimiters может содержать не единственный разделитель, а целый набор разделителей.

import re

def multiple_split(string,delimiters):
    delimeters = list(map(re.escape,delimiters))
    delimeters = '|'.join(delimeters)
    print('d', delimeters)
    result = re.split(fr'{delimeters}',string)
    return result


# Sample Input 1:
#
# print(multiple_split('beegeek-python.stepik', ['.', '-']))
# Sample Output 1:
#
# ['beegeek', 'python', 'stepik']
# Sample Input 2:
#
# print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
# Sample Output 2:
#
# ['Timur', 'Arthur', 'Dima', 'Anri']
# Sample Input 3:
#
# print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))
# Sample Output 3:
#
# ['timur', 'arthur', 'dima', 'anri', 'roma', 'ruslan']

