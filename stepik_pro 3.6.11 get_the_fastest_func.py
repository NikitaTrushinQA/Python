#Функция get_the_fastest_func()
#Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:

#funcs — список произвольных функций
#arg — произвольный объект
#Функция get_the_fastest_func() должна возвращать функцию из списка funcs,
# которая затратила на вычисление значения при вызове с аргументом arg наименьшее количество времени.

import time


def get_the_fastest_func(funcs,arg):
    list_of_time=[]
    for functions in funcs:
        start_time = time.time()
        result=functions(arg)
        end_time = time.time()
        time_func=end_time-start_time
        list_of_time.append(time_func)
    minimum = min(list_of_time)
    return funcs[list_of_time.index(minimum)]





