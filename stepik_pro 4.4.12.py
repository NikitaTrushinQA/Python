#cтуденты курса
#Вам доступен файл students.json, содержащий список JSON-объектов, которые представляют данные о студентах некоторого курса:

#[
 #  {
  #    "name": "Holly-Anne",
  #    "city": "Abilene",
   #   "age": 29,
   #   "progress": 85,
   #   "phone": "(802) 983-9126"
  # },
  # ...
#]
#Под «студентом» мы будем подразумевать один JSON-объект из этого списка. У студента имеются следующие атрибуты:

#name — имя
#city — город проживания
#age — возраст
#progress — прогресс по курсу в процентах
#phone— контактный номер
#Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:

#возраст 18 лет или более
#прогресс по курсу 75% или более
#Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер),
# и записать в него данные выбранных студентов, расположив их в лексикографическом порядке имён.
# В качестве разделителя в файле data.csv должна быть использована запятая.

#Примечание 1. Гарантируется, что все студенты имеют различные имена.

#Примечание 2. Начальная часть файла data.csv выглядит так:

#name,phone
#Cary,(580) 476-8517
#Catarina,(237) 608-2757
#Catherin,(876) 215-3666
#...

import json
import csv

with open('students.json','r',encoding='utf-8') as file1, open ('data.csv','w',newline='') as file2:
    data = json.load(file1)
    result=[]
    for i in data:
        if i['age']>=18 and i['progress']>=75:
            result.append((i['name'],i['phone']))

    columns = ['name','phone']
    writer = csv.writer(file2, delimiter=',')
    writer.writerow(columns)
    for row in sorted(result,key= lambda x:x[0]):
        writer.writerow(row)