#Сотрудники организации3
#Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу,
# которая определяет самого молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней от текущей даты.

#Формат входных данных
#На вход программе в первой строке подается текущая дата в формате DD.MM.YYYY,
# в следующей строке вводится натуральное число n — количество сотрудников, работающих в организации.
# В последующих n строках вводятся данные о каждом сотруднике:
# имя, фамилия и дата рождения, разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.

#Формат выходных данных
#Программа должна определить самого молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней,
# и вывести его имя и фамилию, разделив пробелом. Если таких сотрудников нет, программа должна вывести текст:
#Дни рождения не планируются
#Примечание 1. Гарантируется, что у всех сотрудников даты рождения различны.

#Примечание 2. Например, для даты 01.11.2021 ближайшими семью днями являются:
#02.11.2021, 03.11.2021, 04.11.2021, 05.11.2021, 06.11.2021, 07.11.2021, 08.11.2021

from datetime import date,timedelta,datetime

birthday={}
date_start=datetime.strptime(input(),'%d.%m.%Y')
date_end=date_start +timedelta(days=7)
n = int(input())
for i in range(n):
    name, dat = input().rsplit(' ', 1)
    date = datetime.strptime(dat, '%d.%m.%Y')
    birthday[date] = birthday.setdefault(date, [])+[name]
#print(birthday)
result=[]
for keys,values in birthday.items():
    if date_start < keys.replace(year=date_start.year) <= date_end or date_start < keys.replace(year=date_start.year + 1) <= date_end:
        result.append(keys)
if len(result)!=0:
    the_youngest_worker= birthday.get(max(result))
    print(*the_youngest_worker)
else:
    print('Дни рождения не планируются')