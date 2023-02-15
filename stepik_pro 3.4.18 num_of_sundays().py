from datetime import date, timedelta,datetime

def num_of_sundays(year):
    """Функция принимает год ,
     и возвращает кол-во ворскресений в году"""
    d = datetime(year, 1, 1)
    counter = 0
    if year%100 ==0 and year%400==0:
        for j in range(366):
            d += timedelta(days=1)
            if d.weekday() == 6:
                counter += 1
    elif year%4!=0:
        for i in range(364):
            d+=timedelta(days=1)
            if d.weekday()== 6:
                counter+=1
    else:
        for k in range(366):
            d+=timedelta(days=1)
            if d.weekday()== 6:
                counter+=1
    return counter