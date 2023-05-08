# Требовалось реализовать функцию get_max_index(),
# которая принимает в качестве аргумента список различных целых чисел и возвращает индекс наибольшего числа из этого списка (начиная с 0).
# Программист торопился и реализовал функцию неправильно.

def get_max_index(numbers):
    max_index = 0
    max_value = min(numbers)

    for index, value in enumerate(numbers):
        if value > max_value:
            max_index = index
            max_value = value

    return max_index