
#Поворот матрицы
#Напишите программу, которая поворачивает квадратную матрицу чисел на 90 по часовой стрелке.

#Формат входных данных
#На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

#Формат выходных данных
#Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.

#Тестовые данные 🟢
n = int(input())
m =int(input())
maxi=[]
result=[]
maximum=-1000000
matrix =   [[int(i) for i in input().split()] for j in range(n)]
#print(matrix)
for i in range(n):
    for j in range(m):
        if matrix[i][j]>maximum:
            maximum=matrix[i][j]
for i in range(n):
    for j in range(m):
        if matrix[i][j]==maximum:
            result.append(i)
            result.append(j)
            break
print(result[0],result[1])

2вариант
n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row, col = i, j

print(row, col)
