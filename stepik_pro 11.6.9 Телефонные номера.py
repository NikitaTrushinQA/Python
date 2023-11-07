# Вам доступен набор телефонных номеров, имеющих следующие форматы:
#
# <код страны>-<код города>-<номер>
# <код страны> <код города> <номер>
#
# в котором код страны и код города представлены последовательностями от одной до трех цифр включительно,
# а номер — последовательностью от четырех до десяти цифр включительно.
# Между кодом страны, кодом города и номером используется разделитель, которым служит либо символ дефис, либо пробел,
# причем одновременно оба вида разделителя в одном номере присутствовать не могут.
#
# Напишите программу, которая принимает произвольное количество телефонных номеров и для каждого выводит отдельно его код страны, код города и номер.
#
# Формат входных данных
# На вход программе подается произвольное количество телефонных номеров, удовлетворяющих приведенным выше шаблонам, каждый на отдельной строке.
#
# Формат выходных данных
# Программа должна для каждого введенного телефонного номера вывести отдельно его код страны, код города и номер в следующем формате:
#
# Код страны: <код страны>, Код города: <код города>, Номер: <номер>


import sys
import re

for numbers in sys.stdin:
    p=r'(?P<country>\d{1,3})((-| )?)(?P<city>\d{1,3})\2(?P<num>\d{4,10})'
    match = re.search(p,numbers.strip())

    if match:
        print(f'Код страны: {match.group("country")}, Код города: {match.group("city")}, Номер: {match.group("num")}')



# Sample Input 1:
#
# 1 877 2638277
# 91-011-23413627
# Sample Output 1:
#
# Код страны: 1, Код города: 877, Номер: 2638277
# Код страны: 91, Код города: 011, Номер: 23413627
# Sample Input 2:
#
# 148-809-2561957985
# 1 5 5864
# 91-454-91954
# Sample Output 2:
#
# Код страны: 148, Код города: 809, Номер: 2561957985
# Код страны: 1, Код города: 5, Номер: 5864
# Код страны: 91, Код города: 454, Номер: 91954