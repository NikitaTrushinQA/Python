#Количество секунд
#Напишите программу, которая принимает на вход время и выводит целое количество секунд, прошедшее с начала суток.
#Формат входных данных
#На вход программе подается время в формате HH:MM:SS.
#Формат выходных данных
#Программа должна вывести целое количество секунд, прошедшее с начала суток.
#Примечание 1. Началом суток считается момент времени, соответствующий 00:00:00.

#00:01:01

from datetime import date, timedelta,datetime

my_time = datetime.strptime(input(),'%H:%M:%S')
result=timedelta(hours=my_time.hour,minutes=my_time.minute,seconds=my_time.second)
print(int(result.total_seconds()))
