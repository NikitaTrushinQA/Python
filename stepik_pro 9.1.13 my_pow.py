# Функция my_pow()
# Реализуйте функцию my_pow(), которая принимает один аргумент:
#
# number — целое неотрицательное число
# Функция должна возвращать сумму, состоящую из цифр числа, возведенных в степень их порядкового номера.
#
# Примечание 1. Рассмотрим число 139 из первого теста. Сумма цифр этого числа, возведенных в степень их порядкового номера, равна:
#1**1 + 3**2 + 9 **3 =739

# Sample Input 1:
#
# print(my_pow(139))
# Sample Output 1:
#
# 739
# Sample Input 2:
#
# print(my_pow(123))
# Sample Output 2:
#
# 32
# Sample Input 3:
#
# print(my_pow(0))
# Sample Output 3:
#
# 0

def my_pow(number):
    return sum(map(lambda x: int(x[1])**x[0],enumerate(str(number),start=1)))