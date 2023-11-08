# Популярность
# В онлайн-школе BEEGEEK мы всегда следим за тем, насколько растет наша популярность.
# Для этого мы собираем публикации из различных соцсетей, которые содержат вхождения строки beegeek в нижнем регистре. Мы оцениваем публикацию:
#
# в 3 балла, если она начинается и заканчивается строкой beegeek
# в 2 балла, если она только начинается или только заканчивается строкой beegeek
# в 1 балл, если она содержит строку beegeek только внутри
# в 0 баллов, если она не содержит строку beegeek
#
# Напишите программу, которая определяет популярность онлайн-школы BEEGEEK путем суммирования баллов всех публикаций.
#
# Формат входных данных
# На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.
#
# Формат выходных данных
# Программа должна определить, во сколько баллов оценивается каждая введенная публикация, и вывести сумму всех полученных баллов.

import sys
import re

counter = 0
patt3 = r'^(beegeek).*\1$'
patt2 = r'^((beegeek.*[^beegeek])|([^beegeek].*beegeek))$'
patt1 = r'^.+beegeek.+$'
patt0 =r'beegeek'
for string in sys.stdin:
    if re.fullmatch(patt3,string.strip()):
        counter+=3
    elif re.fullmatch(patt2,string.strip()):
        counter+=2
    elif re.fullmatch(patt1,string.strip()):
        counter+=1
    elif not re.search(patt0,string.strip()):
        counter+=0
    elif re.fullmatch(patt0,string.strip()):
        counter+=2

print(counter)

# Sample Input 1:
#
# hi, beegeek
# beegeek is an awesome place for programmers
# beegeek rocks, rocks beegeek
# i think beegeek is a great place to hangout
# Sample Output 1:
#
# 8
# Sample Input 2:
#
# good morning everyone
# i am going to school
# and it is raining
# Sample Output 2:
#
# 0