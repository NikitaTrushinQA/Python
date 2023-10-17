# Функция ranges() ️
# Будем считать, что последовательность целых неотрицательных чисел можно преобразовать в отрезок,
# если разница между соседними элементами этой последовательности равна единице. Например, числа 3, 4, 5, 6, 7,8 можно преобразовать в отрезок
# [3;8][3;8]. Числа 1, 3, 5, 11, 15, 221,3,5,11,15,22 в отрезок преобразовать нельзя.
# Одиночное число преобразуется в отрезок, в котором и правой, и левой границей является оно само. Например, число 1 можно преобразовать в отрезок [1;1].
#
# Реализуйте функцию ranges(), которая принимает один аргумент:
#
# numbers — список различных натуральных чисел, расположенных в порядке возрастания
# Функция должна преобразовывать числа из списка numbers в отрезки, представляя их в виде кортежей,
# где первый элемент кортежа является левой границей отрезка, второй элемент — правой границей отрезка.
# Полученные кортежи-отрезки функция должна возвращать в виде списка.
#
# Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке.



from itertools import groupby

def ranges(numbers):
    result = [tuple(j) for i,j in groupby(numbers,key=lambda x: numbers.index(x)-x)]
    n=[]
    for i in result:
        n.append((i[0],i[-1]))
    return n

# Sample Input 1:
# numbers = [1, 2, 3, 4, 7, 8, 10]
# print(ranges(numbers))
# Sample Output 1:
# [(1, 4), (7, 8), (10, 10)]
#
# Sample Input 2:
# numbers = [1, 3, 5, 7]
# print(ranges(numbers))
# Sample Output 2:
# [(1, 1), (3, 3), (5, 5), (7, 7)]
#
# Sample Input 3:
# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(ranges(numbers))
# Sample Output 3:
# [(1, 7)]



