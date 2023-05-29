# Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:
#
# number — натуральное число
# Функция должна выводить все цифры числа number, начиная с младших разрядов, каждое на отдельной строке.
#
# Sample Input 1:
#
# print_digits(12345)
# Sample Output 1:
#
# 5
# 4
# 3
# 2
# 1
# Sample Input 2:
#
# print_digits(7)
# Sample Output 2:
#
# 7

def print_digits(number):
    lst = str(number)
    def func(start):
        if start >=0:
            print(lst[start])
            return func(start -1)
    func(len(lst)-1)

