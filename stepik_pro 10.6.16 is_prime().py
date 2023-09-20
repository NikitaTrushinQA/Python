# Функция is_prime()
# Реализуйте функцию is_prime() с использованием генераторных выражений, которая принимает один аргумент:
#
# number — натуральное число
# Функция должна возвращать True, если число number является простым, или False в противном случае.
#
# Примечание 1. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя.

from collections import Counter
def is_prime(number):
    if number ==1:
        return False
    return  True if Counter(number%i==0 for i in range(2,number+1))[True]==1 else False