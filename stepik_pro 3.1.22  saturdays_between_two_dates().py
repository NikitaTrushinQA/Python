#Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:

#start — начальная дата, тип date
#end — конечная дата, тип date
#Функция должна возвращать количество суббот между датами start и end включительно.

#Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.

#Sample Input 1:

#date1 = date(2021, 11, 1)
#date2 = date(2021, 11, 22)

#print(saturdays_between_two_dates(date1, date2))
#Sample Output 1:
#3


from datetime import date

def saturdays_between_two_dates(start,end):
    counter = 0
    if start > end:
        start, end = end, start
    for i in range(date.toordinal(start),date.toordinal(end)+1):
        a = date.fromordinal(i)
        if a.weekday() == 5:
            counter +=1

    return counter