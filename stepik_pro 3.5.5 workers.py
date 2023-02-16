#Сотрудники организации
#Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Напишите программу, которая определяет самого старшего сотрудника из данного списка.

#Формат входных данных
#На вход программе в первой строке подается натуральное число n — количество сотрудников, работающих в организации.
# В последующих nn строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом.
# Дата рождения указывается в формате DD.MM.YYYY.

#Формат выходных данных
#Программа должна определить самого старшего сотрудника и вывести его дату рождения, имя и фамилию, разделив пробелом.
# Если таких сотрудников несколько, программа должна вывести их дату рождения, а также их количество, разделив пробелом.

#Примечание 1. Гарантируется, что у всех сотрудников имена и фамилии различны.
#Sample Input 1:
#3
#Иван Петров 01.05.1995
#Петр Сергеев 29.04.1995
#Сергей Иванов 01.01.1996
#Sample Output 1:
#29.04.1995 Петр Сергеев
#Sample Input 2:
#3
#Иван Петров 01.05.1995
#Петр Сергеев 29.05.1995
#Сергей Иванов 01.05.1995
#Sample Output 2:
#01.05.1995 2

from datetime import date,timedelta,datetime

n=int(input())
list_of_workers=[]
birthday={}
for i in range(n):
    name, dat = input().rsplit(' ', 1)
    date = datetime.strptime(dat, '%d.%m.%Y')
    birthday[date] = birthday.setdefault(date, [])+[name]
max_list=[]
#находим самую маленькую дату
for key in birthday.keys():
    max_list.append(datetime.toordinal(key))
maximum_day=date.fromordinal(min(max_list))
oldest= datetime.strptime(maximum_day.strftime('%d.%m.%Y'), '%d.%m.%Y')
result=birthday.get(oldest)
if len(result) ==1:
    print(oldest.strftime('%d.%m.%Y') ,result[0],sep=' ')
else:
    print(oldest.strftime('%d.%m.%Y'), len(result), sep=' ')




