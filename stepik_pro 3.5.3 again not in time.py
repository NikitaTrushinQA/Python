#Снова не успел
#Дан режим работы магазина:

#Понедельник	9:00 - 21:00
#Вторник	9:00 - 21:00
#Среда	9:00 - 21:00
#Четверг	9:00 - 21:00
#Пятница	9:00 - 21:00
#Суббота	10:00 - 18:00
#Воскресенье	10:00 - 18:00
#Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут,
# оставшееся до закрытия магазина.

#Формат входных данных
#На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

#Формат выходных данных
#Программа должна вывести количество минут, которое осталось до закрытия магазина,
# или текст Магазин не работает, если он закрыт.

from datetime import date,timedelta,datetime

schedule = {0: (timedelta(hours=9), timedelta(hours=21)),
            1: (timedelta(hours=9), timedelta(hours=21)),
            2: (timedelta(hours=9), timedelta(hours=21)),
            3: (timedelta(hours=9), timedelta(hours=21)),
            4: (timedelta(hours=9), timedelta(hours=21)),
            5: (timedelta(hours=10), timedelta(hours=18)),
            6: (timedelta(hours=10), timedelta(hours=18))}


def minutes_before_closing(now):
    result=0
    datetimenow=now.split(' ')
    datenow=datetimenow[0].split('.')
    datenow2=date(int(datenow[2]),int(datenow[1]),int(datenow[0]))
    now_time = list(map(lambda x: int(x), datetimenow[1].split(':')))
    timedelta_now_time = timedelta(hours=now_time[0], minutes=now_time[1])
    weekday = datenow2.weekday()
    timeperiod = schedule[weekday]
    if timeperiod[0]<=timedelta_now_time<timeperiod[1]:
        result = (timeperiod[1].seconds/60-timedelta_now_time.seconds/60)
        return int(result)
    else:
        return 'Магазин не работает'

now=input()  #07.11.2021 10:00
print(minutes_before_closing(now))