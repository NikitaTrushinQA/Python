
#Умножение матриц
#Напишите программу, которая перемножает две матрицы.

#Формат входных данных
#На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице,
#затем элементы первой матрицы, затем пустая строка. Далее следуют числа mm и kk — количество строк и столбцов второй матрицы затем элементы второй матрицы.

#Формат выходных данных
#Программа должна вывести результирующую матрицу, разделяя элементы символом пробела

n, m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
stroka=input()
m, k = [int(i) for i in input().split()]
matrix2 = [[int(i) for i in input().split()] for _ in range(m)]
matrix3 = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for h in range(m):
            matrix3[i][j]+=matrix1[i][h]*matrix2[h][j]
for r in range(n):
    for c in range(k):
        print(matrix3[r][c], end=' ')
    print()


