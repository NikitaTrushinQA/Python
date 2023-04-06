
#Контрольная сумма
#По каналу связи передаются pickle файл, содержащий сериализованный словарь или список, и целое число — контрольная сумма,
# которая вычисляется по следующему правилу:

#для словаря — сумма всех целочисленных ключей (тип int)
#для списка — произведение минимального и максимального целочисленных элементов (тип int)
#Напишите программу, которая вычисляет контрольную сумму для объекта, содержащегося в pickle файле, и сравнивает ее с данным целым числом.

#Формат входных данных
#На вход программе в первой строке подается название pickle файла, в котором содержится сериализованный словарь или список, в следующей — целое число.

#Формат выходных данных
#Программа должна вычислить контрольную сумму для объекта, который содержится в данном pickle файле, и

#если она совпадает с введенным числом, вывести текст:
#Контрольные суммы совпадают

#если она не совпадает с введенным числом, вывести текст:
#Контрольные суммы не совпадают

#Примечание 1. Если список (словарь) не содержит целочисленных элементов (ключей), то считайте, что контрольная сумма равна 0.

#Примечание 2. Рассмотрим первый тест. Подается название файла — data.pkl, в котором содержится сериализованный список:

#['a', 'b', 3, 4, 'f', 'g', 7, 8]
#затем число — 3023. Контрольная сумма для данного списка равна 3 * 8 = 24. Так как 3023!=24
#программа выводит:

#Контрольные суммы не совпадают

import pickle

file=input()
code=int(input())

with open(file,'rb') as file1:
    obj = pickle.load(file1)
    if type(obj)==list:
        obj=list(filter(lambda x: type(x) == int, obj))
        result=max(obj,default=0) * min(obj,default=0)
    elif type(obj)==dict:
        result=sum(list(filter(lambda x: type(x) == int, obj.keys())))
    if result==code:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')