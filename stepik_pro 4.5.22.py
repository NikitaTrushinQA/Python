#Вам доступен архив data.zip, содержащий различные папки и файлы.
#Среди них есть несколько JSON файлов, каждый из которых содержит информацию о каком-либо футболисте:

#{
#   "first_name": "Gary",
#   "last_name": "Cahill",
#   "team": "Chelsea",
#   "position": "Defender"
#}
#У футболиста имеются следующие атрибуты:

#first_name — имя
#last_name — фамилия
#team — название футбольного клуба
#position — игровая позиция
#Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих за футбольный клуб Arsenal.
#Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.

#Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным текстовым файлом в формате JSON.
#Для того чтобы определить, является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь конструкцией try-except и функцией is_correct_json()


from zipfile import ZipFile
import json

def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False

with ZipFile('data.zip', mode='r') as zip_file:
    result=[]
    info = zip_file.infolist()
    for i in info:
        if i.filename.endswith('.json') :
            with zip_file.open(i.filename) as file1:
                try :
                    is_correct_json(file1)
                    data=file1.read().decode('utf-8')
                    if is_correct_json(data):
                        d = json.loads(data)
                        if d['team']=='Arsenal':
                            result.append([d["first_name"], d["last_name"]])
                except:
                    pass

    result=sorted(result,key=lambda x:(x[0],x[1]))
    for name,sunname in result:
        print(name,sunname)



