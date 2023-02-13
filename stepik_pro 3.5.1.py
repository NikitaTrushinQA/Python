#Во время решения очередной задачи программист фиксирует время начала и окончания ее решения и добавляет полученные результаты в список data.
#Каждый результат представляет собой кортеж, первым элементом которого является время начала решения в виде строки в формате HH:MM,
#вторым элементом — время окончания решения в виде строки в том же формате.
#Дополните приведенный ниже код, чтобы он вывел общее целое количество минут, которое программист затратил на решение всех задач.


from datetime import date, time, datetime, timedelta
import time
data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

sum_minutes=0
for start,end in data:
        start_string = start.split(':')
        end_string = end.split(':')
        new_start = timedelta(hours=int(start_string[0]), minutes=int(start_string[1]))
        new_end = timedelta(hours=int(end_string[0]), minutes=int(end_string[1]))
        delta = new_end - new_start
        sum_minutes+=int(delta.total_seconds()/60)
print(sum_minutes)


