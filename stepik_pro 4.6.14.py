#Реализуйте функцию filter_dump(), которая принимает три аргумента в следующем порядке:

#filename — название pickle файла, например, data.pkl
#objects — список произвольных объектов
#typename — тип данных
#Функция должна создавать pickle файл с названием filename, который содержит сериализованный список только тех объектов из списка objects,
# тип которых равен typename.

#Примечание 1. Например, вызов функции filter_dump() следующим образом:

#filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
#должен создавать файл numbers.pkl, содержащий сериализованный список [1, 3, 4].



import pickle

def filter_dump(filename,object,typename):
    with open(filename,'wb') as file1:
        lst = list(filter(lambda x: type(x) == typename, object))
        pickle.dump(lst, file1)


print(filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int))