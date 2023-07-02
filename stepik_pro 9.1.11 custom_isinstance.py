# Функция custom_isinstance()
# Реализуйте функцию custom_isinstance(), которая принимает два аргумента в следующем порядке:
#
# objects — список произвольных объектов
# typeinfo — тип данных или кортеж с типами
# Функция должна возвращать единственное число — количество объектов из списка objects, которые принадлежат типу typeinfo или одному из типов, если был передан кортеж.
#
# Примечание 1. В задаче удобно воспользоваться функцией isinstance().

#
# Sample Input 1:
#
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, int))
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, (int, float)))
# Sample Output 2:
#
# 4

def custom_isinstance(objects,typeinfo):
    return [isinstance(i,typeinfo) for i in objects].count(True)