#Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о странах и исповедуемых
# в них религиях:

#[
  # {
  #    "country": "Afghanistan",
  #    "religion": "Islam"
 #  },
 #  {
 #     "country": "Albania",
#      "religion": "Islam"
#   },
#   ...
#]
#Каждый объект из этого списка содержит два атрибута:

#country — страна
#religion — исповедуемая религия
#Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии,
# а в качестве значения — список стран, в которых исповедуется данная религия.
# Полученный JSON-объект программа должна записать в файл religion.json.

#Примечание 1. Страны в списках должны располагаться в своем исходном порядке.

#Примечание 2. Начальная часть файла religion.json выглядит так:

#{
  # "Islam":[
   #   "Afghanistan",
  #    "Albania",
   #   "Algeria",
   #   ...
  # ],
  # ...
#}

import json

with open('countries.json','r') as file1, open ('religion.json','w') as file2:
    data = json.load(file1)
    d={}
    for i in data:
        d[i['religion']] = d.get(i['religion'], []) + [i['country']]
    json.dump(d, file2,indent=3)