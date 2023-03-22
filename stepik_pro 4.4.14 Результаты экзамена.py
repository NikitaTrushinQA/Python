#Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором учебном заведении.
# В первом столбце записано имя студента,
# во втором — фамилия,
# в третьем — оценка за экзамен,
# в четвертом — дата и время сдачи в формате YYYY-MM-DD HH:MM:SS,
# в пятом — адрес электронной почты:

#name,surname,score,date_and_time,email
#Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
#April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
#...
#Каждый студент имеет право пересдать экзамен два раза,
# поэтому он может встречаться в исходном файле до трёх раз с различной оценкой и различными датой и временем сдачи.

#Напишите программу, которая для каждого студента определяет его максимальную оценку, а также дату и время ее получения.
# Программа должна создать список словарей, каждый из которых содержит следующие пары ключ-значение:

#name — имя студента
#surname — фамилия студента
#best_score — максимальная оценка за экзамен
#date_and_time — дата и время получения максимальной оценки в исходном формате
#email — адрес электронной почты
#Полученный список программа должна записать в файл best_scores.json,
# причем словари в списке должны быть расположены в лексикографическом порядке названий электронных почт.

#Примечание 1. Если при пересдаче студент получил такую же оценку, что и в прошлый раз, то в качестве даты следует указать дату пересдачи.

#Примечание 2. В качестве разделителя в файле exam_results.csv используется запятая, при этом кавычки не используются.

#Примечание 3. Начальная часть файла best_scores.json выглядит так:

#[
 #  {
  #    "name": "Stephen",
   #   "surname": "Farley",
    #  "best_score": 3,
     # "date_and_time": "2021-11-12 12:00:00",
      #"email": "aardo@mac.com"
   #},
   #{
   #   "name": "Kaylen",
    #  "surname": "Horne",
     # "best_score": 4,
      #"date_and_time": "2021-11-09 11:00:00",
     # "email": "aaribaud@att.net"
   #},
   #...
#]

import json
import csv
from datetime import datetime

with open('exam_results.csv','r',encoding='UTF-8') as file1, open ('best_scores.json','w',encoding='UTF-8') as file2:
    data = list(csv.reader(file1))
    d= []
    d2 =[]
    for persona in data[1:]:
        d.append({'name': persona[0], 'surname': persona[1], 'best_score': int(persona[2]),
                  'date_and_time': datetime.strptime(persona[3], '%Y-%m-%d %H:%M:%S'), 'email': persona[4]})
    result = sorted(d,key=lambda x:(x['email'],x['best_score'],x['date_and_time']),reverse=True)
    d2.append(result[0])
    d2[0]['date_and_time']=d2[0]['date_and_time'].strftime('%Y-%m-%d %H:%M:%S')
    for i in range(1,len(result)):
        if result[i]['email'] != result[i-1]['email']:
            result[i]['date_and_time']=(result[i].get('date_and_time')).strftime('%Y-%m-%d %H:%M:%S')
            d2.append(result[i])
    json.dump(sorted(d2,key=lambda x:x['email']), file2,indent=3)