# Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая проходит в четвертый четверг месяца.
#
# Напишите программу, которая определяет день проведения очередной встречи питонистов в Сан-Диего.
#
# Формат входных данных
# На вход программе подается два натуральных числа, представляющие год и месяц, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна определить день проведения встречи в Сан-Диего в указанных году и месяце и вывести результат в формате DD.MM.YYYY.


import calendar
from datetime import datetime,date

y = int(input())
m = int(input())
counter = 0
for i in calendar.monthcalendar(year=y, month=m):
    for index,j in enumerate(i,start=1):
        if index==4 and j!=0:
            counter+=1
            if counter==4:
                print(date(year=y,month=m,day=j).strftime('%d.%m.%Y'))
                break


# Sample Input 1:
#
# 2012
# 3
# Sample Output 1:
#
# 22.03.2012
# Sample Input 2:
#
# 2015
# 2
# Sample Output 2:
#
# 26.02.2015
# Sample Input 3:
#
# 2018
# 6
# Sample Output 3:
#
# 28.06.2018