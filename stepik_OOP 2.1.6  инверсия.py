# функция inversions()

# Дана последовательность чисел a1,a2,a3...an.  Назовем пару (ai,aj)  инверсией, если i <j, a  ai>aj.
# Например, последовательность 3, 1, 4,2 имеет три инверсии (3,1), (3, 2), (4, 2).
# Каждая инверсия — это пара элементов, нарушающих порядок.
#
# реализуйте функцию inversions(), которая принимает один аргумент:
#
# sequence — последовательность, элементами которой являются числа
# Функция должна возвращать единственное число — количество инверсий в последовательности sequence.
#
# Примечание 1. Последовательностью будем считать объект, имеющий длину и поддерживающий индексацию.
# Например, объекты типа list или range являются последовательностями.

from itertools import combinations


def inversions(sequence: list[int]) -> int:
    result = 0
    for seq in combinations(sequence, 2):
        current_item, next_item = seq
        if current_item > next_item:
            result += 1
    return result

# Sample Input 1:
#
# sequence = [3, 1, 4, 2]
#
# print(inversions(sequence))
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# sequence = [1, 2, 3, 4, 5]
#
# print(inversions(sequence))
# Sample Output 2:
#
# 0
# Sample Input 3:
#
# sequence = [4, 3, 2, 1]
#
# print(inversions(sequence))
# Sample Output 3:
#
# 6
# Sample Input 4:
#
# sequence = [1, 1, 1, 1, 1, 1]
#
# print(inversions(sequence))
# Sample Output 4:
#
# 0