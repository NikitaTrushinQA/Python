# Функция print_digits()
# Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:
#
# number — натуральное число
# Функция должна выводить все цифры числа number, начиная со старших разрядов, каждое на отдельной строке.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_digits(),
# но не код, вызывающий ее.

def print_digits(number):
    lst = str(number)
    def func(start):
        if start <len(lst):
            print(lst[start])
            return func(start +1)
    func(0)

print_digits(12345)