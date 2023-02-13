#Пятница, 13-е
#Докажите, что 13-е число месяца чаще всего приходится на пятницу.
#Напишите программу, которая вычисляет,
# сколько тринадцатых чисел приходится на каждый день недели в период с 01.01.0001 по 31.12.9999.
#Формат входных данных
#На вход программе ничего не подается.

#Формат выходных данных
#Программа должна вывести 7 чисел — количество тринадцатых чисел,
# которые приходятся на понедельник, вторник, среду, четверг, пятницу, субботу и воскресенье в период с 01.01.0001 по 31.12.9999.
# Числа должны быть расположены каждое на отдельной строке.
#ответ:
#17123
#17124
#17173
#17097
#17199
#17099
#17173

from datetime import date,timedelta
date1 = date(1, 1, 1)
date2 = date(9999, 12, 31)
d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0} #словарик для подсчета на какой день недели падает 13у число
while date1!=date(9999, 12, 31):
    date1+=timedelta(days=1)
    if date1.day==13:
        d[date1.weekday()]=d.get(date1.weekday(), 0) + 1

for keys,values in d.items():
    #print(values)

