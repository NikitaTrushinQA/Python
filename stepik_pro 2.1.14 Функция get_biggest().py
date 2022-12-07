#Функция get_biggest()
#Реализуйте функцию get_biggest(), которая принимает один аргумент:

#numbers — список целых неотрицательных чисел
#Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers.
# Если список numbers пуст, функция должна вернуть число -1.

#Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3], из которых можно составить следующие числа:
#123, 132, 213, 231, 312, 321
#Наибольшим из представленных является 3213.

def get_biggest(numbers):
    n = len(numbers)
    if n > 0:
        digit_max_len = len(str(max(numbers)))
        sorted_numbers = sorted(numbers, key=lambda x: str(x) * digit_max_len, reverse=True) #сортируем по первой цифре в реверсе
        result = list(map(str,sorted_numbers))
        return int(''.join(result))
    else:
        return -1








