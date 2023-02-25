#Реализуйте функцию get_all_mondays(), которая принимает один аргумент:

#year — натуральное число
#Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на понедельник.

import calendar
from datetime import datetime,timedelta,date


def get_all_mondays(year):
    result = []
    start=datetime(year=year,month=1,day=1)
    leap=calendar.isleap(year)
    if leap:
        for i in range(0, 366):
            if (date(year=start.year, month=start.month, day=1) + timedelta(days=i)).weekday()==0:
                result.append(date(year=start.year, month=start.month, day=1) + timedelta(days=i))
    else:
        for j in range(0, 365):
            if (date(year=start.year, month=start.month, day=1) + timedelta(days=j)).weekday() == 0:
                result.append(date(year=start.year, month=start.month, day=1) + timedelta(days=j))
    return result

#2вариант
#def get_all_mondays(year):
    #mondays = []
    #for month in range(1, 13):
        #for week in calendar.monthcalendar(year, month):
            #monday = week[0]
            #if monday:
                #mondays.append(date(year, month, monday))
    #return mondays


#print(get_all_mondays(111))