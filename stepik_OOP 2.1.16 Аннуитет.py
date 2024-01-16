# Реализуйте генераторную функцию annual_return(), которая принимает три аргумента в следующем порядке:
#
#     start — целое число, начальная сумма вклада в рублях
#     percent — целое число, процент, на который текущая сумма вклада будет увеличиваться каждый год
#     years — целое число, количество лет, в течение которых будут начисляться проценты
#
# Функция должна возвращать итератор, моделирующий банковский вклад.
# Возвращаемыми значениями итератора должны являться размеры вклада после очередного начисления процентов percent.

def annual_return(start,percent,years):

    for i in range(years):
        start *=(1.0+percent/100)
        yield start




# Sample Input 1:
#
# for value in annual_return(120000, 10, 3):
#     print(round(value))
#
# Sample Output 1:
#
# 132000
# 145200
# 159720
#
# Sample Input 2:
#
# for value in annual_return(70000, 8, 10):
#     print(round(value))
#
# Sample Output 2:
#
# 75600
# 81648
# 88180
# 95234
# 102853
# 111081
# 119968
# 129565
# 139930
# 151125

