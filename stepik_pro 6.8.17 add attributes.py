# Вам доступна переменная data, содержащая Counter словарь. Дополните приведенный ниже код, чтобы он добавил этому словарю два атрибута:
#
# min_values() — функция, которая возвращает список элементов, имеющих наименьшее значение
# max_values() — функция, которая возвращает список элементов, имеющих наибольшее значение
# Обе функции не должны принимать никаких аргументов.
#
# Примечание 1. Элементом словаря будем считать кортеж (ключ, значение).
#
# Примечание 2. Элементы словаря в возвращаемых функциями списках должны располагаться в своем исходном порядке.
#
# Примечание 3. Функции data.min_values() и data.max_values() должны учитывать содержимое словаря.
# Например, если в словарь data будет добавлена новая пара ключ-значение,
# то и в возвращаемых функциями списках данные ключ и значение должны присутствовать.
# Sample Input 1:
# print(data.max_values())
# Sample Output 1:
# [('j', 8), ('q', 8)]
#
# Sample Input 2:
# print(data.min_values())
# Sample Output 2:
# [('t', 1)]

from collections import Counter


def Func_min():
    result = [(key, value) for key, value in data.items() if value == min(data.values())]
    return result


def Func_max():
    result = [(key, value) for key, value in data.items() if value == max(data.values())]
    return result


data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
data.min_values = Func_min
data.max_values = Func_max