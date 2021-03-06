
#Заполнение 1
#На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m и заполняет её числами от 1 до n  в соответствии с образцом.

#Формат входных данных
#На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

#Формат выходных данных
#Программа должна вывести матрицу в соответствии с образцом.

#Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент.
# Для этого используйте строковый метод ljust().

nm=input().split()
n=int(nm[0])
m=int(nm[1])
matrix = [[0] * m for _ in range(n)]
counter=0
for i in range(n):
    for j in range(m):
        counter+=1
        matrix[i][j]=counter
        print(str(matrix[i][j]).ljust(3), end='')
    print()