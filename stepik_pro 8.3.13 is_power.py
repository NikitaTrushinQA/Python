# Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:
#
# number — натуральное число
# Функция должна возвращать значение True, если number является степенью числа 22, или False в противном случае.

def is_power(number):
    if number==1 or number==2:
        return True
    elif number<2:
        return False
    else:
        return is_power(number/2)