#функция get_days_in_month(), которая принимает два аргумента в следующем порядке:
#year — натуральное число
#month — полное название месяца на английском
#Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.

import calendar
from datetime import datetime,timedelta,date


def get_days_in_month(year,month):
    result=[]
    string = f'{year} {month}'
    d = datetime.strptime(string, '%Y %B')
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    for i in range(0,days_in_month):
        result.append(date(year=d.year,month=d.month,day=1)+timedelta(days=i))
    return result