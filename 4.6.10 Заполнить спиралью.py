#Заполнение спиралью
#На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m заполнив её "спиралью" в соответствии с образцом.

#Формат входных данных
#На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

#Формат выходных данных
#Программа должна вывести матрицу в соответствии образцом.

n, m = (int(i) for i in input().split())
spiral = []
x, y, dx, dy, k = 0, 0, 1, 0, 1
spiral = [[0]* n for _ in range(m)]
for i in range(1, n * m + 1):
    spiral[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < m and 0 <= ny < n and spiral[nx][ny] == 0:
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x + dx, y + dy
for i in range(n):
    for j in range(m):
        print(str(spiral[j][i]).ljust(3), end=' ')
    print()
