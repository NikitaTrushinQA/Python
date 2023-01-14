
#реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:

#start — начальная дата, тип date
#end — конечная дата, тип date
#Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно. Если start > end, функция должна вернуть пустой список.

#Sample Input 1:

#date1 = date(2021, 10, 1)
#date2 = date(2021, 10, 5)

p#rint(*get_date_range(date1, date2), sep='\n')
#Sample Output 1:

#2021-10-01
#2021-10-02
#2021-10-03
#2021-10-04
#2021-10-05





from datetime import date


def get_date_range(date1,date2):
    result =[]
    for i in range(date.toordinal(date1),date.toordinal(date2)+1):
        a = date.fromordinal(i)
        result.append(a)
    return result