#  Функция get_all_values()
# Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:
#
# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект
# Функция должна возвращать множество, элементами которого являются все значения по ключу key из всех словарей в chainmap.
#  Если ключ key отсутствует в chainmap, функция должна вернуть пустое множество.
#
# Примечание 1. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит словари с хешируемыми значениями.

# Sample Input 1:
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# result = get_all_values(chainmap, 'name')
#
# print(*sorted(result))

# Sample Output 1:
# Arthur Timur

# Sample Input 2:
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# result = get_all_values(chainmap, 'age')

# print(result)
# Sample Output 2:
# set()

from collections import ChainMap
def get_all_values(chainmap,key):
    result=set()
    for dct in chainmap.maps:
        for k,v in dct.items():
            search = dct.get(key)
            if search != None:
                result.add(search)
    return result
