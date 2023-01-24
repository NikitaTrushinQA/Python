#напишите программу, которая принимает на вход дату и выводит предыдущую и следующую даты.

#Формат входных данных
#На вход программе подается дата в формате DD.MM.YYYY.

#Формат выходных данных
#Программа должна вывести предыдущую и следующую даты относительно введенной даты, каждую на отдельной строке, в формате DD.MM.YYYY.

#Примечание 1. Гарантируется, что у подаваемой даты есть предыдущая и следующая даты.

from datetime import date, timedelta,datetime

my_date=input()
my_date = datetime.strptime(my_date,'%d.%m.%Y')
date1 = my_date -timedelta(days=1)
date2=my_date+timedelta(days=1)
print(datetime.strftime(date1,'%d.%m.%Y'))
print(datetime.strftime(date2,'%d.%m.%Y'))