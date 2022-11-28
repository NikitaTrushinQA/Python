#функция index_of_nearest()
#Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:

#numbers — список целых чисел
#number — целое число
#Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс.
# Если список numbers пуст, функция должна вернуть число -1−1.

#Примечание 1. Если в функцию передается список, содержащий несколько чисел, одновременно являющихся ближайшими к искомому числу,
# функция должна возвращать наименьший из индексов ближайших чисел.

#Примечание 2. Рассмотрим третий тест. Ближайшими числами к числу 4 являются 5 и 3, имеющие индексы 1 и 2 соответственно. Наименьший из индексов равен 1.

def index_of_nearest(numbers,number):
    min_delta = []
    if numbers ==[]:
        return -1
    else:
        for i in numbers:
            min_dif = abs(number - i)
            min_delta.append(min_dif)
        min_number = min(min_delta)
        result = min_delta.index(min_number)
        return result




