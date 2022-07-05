#Возведение матрицы в степень
#Напишите программу, которая возводит квадратную матрицу в m-ую степень.

#Формат входных данных
#На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число mm.

#Формат выходных данных
#Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

#Тестовые данные 🟢



def umnmatr(n):
    for i in range(n):
        for j in range(n):
            for h in range(n):
                matrix3[i][j]+=matrix[i][h]*matrix[h][j]
    return matrix3

n =int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
matrix3 = [[0] * n for _ in range(n)]

for i in umnmatr(n):
 print(*i)