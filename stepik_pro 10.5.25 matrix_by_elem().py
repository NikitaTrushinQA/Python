# Функция matrix_by_elem()
# Вам доступна генераторная функция matrix_by_elem(), которая принимает в качестве аргумента матрицу произвольной размерности и возвращает генератор,
# порождающий последовательность элементов переданной матрицы.
#
# Перепишете данную функцию с использованием конструкции yield from, чтобы она выполняла ту же задачу.
#
# Примечание 1. Под матрицей подразумеваются исключительно вложенные списки.

def matrix_by_elem(matrix):
    for row in matrix:
        yield from row

# Sample Input:
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(*matrix_by_elem(matrix))
# Sample Output:
#
# 1 2 3 4 5 6 7 8 9