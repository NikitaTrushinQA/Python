#Напишите программу, которая определяет количество дней в заданном месяце.

#Формат входных данных
#На вход программе подаются год и полное название месяца на английском, разделенные пробелом.
#Формат выходных данных
#Программа должна вывести единственное число — количество дней в введенном месяце.

#Sample Input 1:
#1983 January
#Sample Output 1:
#31
#Sample Input 2:
#1956 February
#Sample Output 2:
#29
#Sample Input 3:
#1959 March
#Sample Output 3:
#31

import calendar
from datetime import  datetime
string =input()
d = datetime.strptime(string,'%Y %B')
days = calendar.monthrange(d.year, d.month)[1]
print(days)