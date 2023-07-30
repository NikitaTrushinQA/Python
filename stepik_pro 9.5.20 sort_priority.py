# Функция sort_priority()
# Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:
#
# values — список чисел
# group — список, кортеж или множество чисел

# Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group, которая должна следовать первой.

# Sample Input 1:
# numbers = [8, 3, 1, 2, 5, 4, 7, 6]
# group = {5, 7, 2, 3}
# sort_priority(numbers, group)
# print(numbers)
# Sample Output 1:
# [2, 3, 5, 7, 1, 4, 6, 8]
#
# Sample Input 2:
# numbers = [150, 200, 300, 1000, 50, 20000]
# sort_priority(numbers, [300, 100, 200])
# print(numbers)
# Sample Output 2:
# [200, 300, 50, 150, 1000, 20000]
#
# Sample Input 3:
# numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# sort_priority(numbers, (300, 100, 200))
# print(numbers)
# Sample Output 3:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sort_priority(numbers, group):
    numbersMax = max(numbers)
    groupMax = max(group)
    numbers.sort(key=lambda x: x if x in group else x + groupMax + numbersMax)
    return numbers

#или
#def sort_priority(numbers, group):
#    numbers.sort(key=lambda x: (x not in group, x))
