#Вам доступен файл data.json, содержащий список различных объектов:

#[
#   "nwkWXma",
#   null,
#   {
#      "ISgHT": "dIUbf"
#   },
#   "Pzt",
#   "BXcbGVTE",
#   ...
#]
#Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле data.json,
# измененные по следующим правилам:

#если объект является строкой, в его конец добавляется восклицательный знак
#если объект является числом, он увеличивается на единицу
#если объект является логическое значением, он инвертируется
#если объект является списком, он удваивается
#если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
#если объект является пустым значением (null), он не добавляется
#Полученный список программа должна записать в файл updated_data.json.

#Примечание 1. Например, если бы файл data.json имел вид:

#["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
#то программа должна была бы создать файл updated_data.json со следующим содержанием:

#["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]

import json

with open('data.json','r') as file:
    result=[]
    data = json.load(file)
    for items in data:
        if type(items)==str:
            result.append(items+'!')
        elif type(items)==int:
            result.append(items + 1)
        elif type(items)==bool:
            if items==False:
                result.append(True)
            else:
                result.append(False)
        elif type(items)==list:
            result.append(items*2)
        elif type(items)==dict:
            items.update({"newkey": None})
            result.append(items)

        with open('updated_data.json', 'w') as file2:
            json.dump(result, file2)