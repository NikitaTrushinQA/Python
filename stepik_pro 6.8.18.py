# Here we go again
# Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя.
# В первом столбце записано измененное имя пользователя,
# во втором — адрес электронной почты,
# в третьем — дата и время изменения.
#
# При этом email пользователь менять не может, только имя:
#
# username,email,dtime
# rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
# busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
# ...
# Напишите программу, которая определяет, сколько раз пользователь менял имя.
# Программа должна вывести адреса электронных почт пользователей, указав для каждого соответствующее количество смененных имен.
# Почтовые ящики должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
#
# <адрес электронной почты>: <количество изменений имен>
# Примечание 1. Начальная часть ответа выглядит так:
#
# barbaraanderson@bk.ru: 3
# barbarabrown@rambler.ru: 3
...

from collections import Counter
import csv

with open('name_log.csv',encoding='UTF-8') as file:
    rows = list(csv.reader(file))
    del rows[0]
    rows = list(map(lambda x:x[1],rows))
    result = Counter(rows)
    for email,num in sorted(result.items()):
        print(f'{email}: {num}')