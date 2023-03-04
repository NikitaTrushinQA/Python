#Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя.
# В первом столбце записано измененное имя пользователя,во втором — адрес электронной почты,
# в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:

#username,email,dtime
#rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
#busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
#...
#Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для каждого пользователя и записывает их в файл new_name_log.csv.
# В файле new_name_log.csv первой строкой должны быть заголовки столбцов такие же, как в файле name_log.csv.
# Логи в итоговом файле должны быть расположены в лексикографическом порядке названий электронных ящиков пользователей.

#Примечание 1. Для части пользователей в исходном файле запись только одна, и тогда в итоговый файл следует записать только ее,
# для некоторых пользователей есть несколько записей с разными именами.

#Например, пользователь с электронной почтой c3po@gmail.com несколько раз менял имя:

#C=3PO,c3po@gmail.com,16/11/2021 17:10
#C3PO,c3po@gmail.com,16/11/2021 17:15
#C-3PO,c3po@gmail.com,16/11/2021 17:24
#Из этих трех записей в итоговый файл должна быть записана только одна — самая свежая:

#C-3PO,c3po@gmail.com,16/11/2021 17:24
#Примечание 2. Разделителем в файле name_log.csv является запятая, при этом кавычки не используются.

import csv
from datetime import datetime

with open ('name_log.csv', 'r', encoding='utf-8') as file1, open ('new_name_log.csv','w',encoding='utf-8',newline='') as file2:
    rows = list(csv.reader(file1))
    columns=['username','email','dtime']
    rows = rows[1::]
    d = {}
    for line in rows:
        line[2]=datetime.strptime(line[2], "%d/%m/%Y %H:%M")
    sorted_rows=sorted(rows, key=lambda x: x[2])
    for j in sorted_rows:
        d[j[1]]=[j[0],j[1],datetime.strftime(j[2],"%d/%m/%Y %H:%M")]
    result=[]
    for values in d.values():
        result.append(values)
    sorted_result=sorted(result,key=lambda x:(x[1]))
    writer = csv.writer(file2)
    writer.writerow(columns)
    for k in sorted_result:  #печатаем в файл в отсортированном списке по email(в лексикографическом порядке)
        writer.writerow(k)
