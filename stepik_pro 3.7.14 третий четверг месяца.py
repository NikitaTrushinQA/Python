#ТЧМ
#Во многих музеях существует один день месяца, когда посещение музея для всех лиц или отдельных категорий граждан происходит без взимания платы.
#Например, в Эрмитаже это третий четверг месяца.

#Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном году.

#Формат входных данных
#На вход программе подается натуральное число, представляющее год.

#Формат выходных данных
#Программа должна определить все даты бесплатных дней посещения Эрмитажа в введенном году и вывести их.
# Даты должны быть расположены в порядке возрастания, каждая на отдельной строке, в формате DD.MM.YYYY.

import calendar
from datetime import date,datetime

year=int(input())
free_days = []
for month in range(1, 13):
    counter=0
    for week in calendar.monthcalendar(year, month):
        thursday = week[3]
        if thursday:
            counter+=1
            if counter==3:
                free_days.append(date(year, month, thursday))
                counter=0
result=list(map(lambda x:datetime.strftime(x,'%d.%m.%Y'),free_days))
print(*result,sep='\n')


