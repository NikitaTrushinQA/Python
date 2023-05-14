# Функция add_to_list_in_dict()
# Реализуйте функцию add_to_list_in_dict() с использованием конструкции try-except, которая принимает три аргумента в следующем порядке:
#
# data — словарь списков, то есть словарь, значением в котором является список
# key — хешируемый объект
# element — произвольный объект
# Функция должна добавлять объект element в список по ключу key в словаре data.
# Если ключа key в словаре data нет, функция должна добавить его в словарь,
# присвоить ему в качестве значения пустой список и добавить в этот список объект element.
#
# Примечание 1. Функция должна изменять переданный словарь и возвращать значение None.
#
# Примечание 2. Элементы в список должны добавляться в конец.

# Sample Input 1:
#
# data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# add_to_list_in_dict(data, 'b', 7)
#
# print(data)
# Sample Output 1:
#
# {'a': [1, 2, 3], 'b': [4, 5, 6, 7]}
# Sample Input 2:
#
# data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# add_to_list_in_dict(data, 'c', 7)
#
# print(data)
# Sample Output 2:
#
# {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7]}

def add_to_list_in_dict(data,key,element):
    try:
        data[key] = data.setdefault(key,[]) +[element]
        return None
    except KeyError:
        pass
