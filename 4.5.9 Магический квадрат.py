
#Магический квадрат
#Магическим квадратом порядка nn называется квадратная таблица размераn×n, составленная из всех чисел 1, 2, 3, ....., n^2
#так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

#Формат входных данных
#На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: n строк, по nn чисел в каждой, разделённые пробелами.

#Формат выходных данных
#Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.


n=int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
Flag=True
diag_main=0
diag_pob=0
stroka=0
list1=[]
stolb=0
list2=[]
new_matrix=[]
counter=0
for i in range(n):
    for j in range(n):
        new_matrix.append(matrix[i][j])
new_matrix.sort()
for k in range(len(new_matrix)):
    if new_matrix[k]==k+1:
        counter+=1
if counter!=n**2:
    Flag=False
    print('NO')
    quit()
for k in range(n):
    diag_main+=matrix[k][k]
    diag_pob=matrix[k][n-k-1]
    if diag_main!=diag_pob:
        Flag=False
        break
for i in range(n):
    stroka=0
    for j in range(n):
        stroka+=matrix[i][j]
    list1.append(stroka)
firs_element = list1[0]
for element in list1:
    if element != firs_element:
        Flag=False
        break
    else:
        Flag=True
for i in range(n):
    stolb=0
    for j in range(n):
        stolb+=matrix[j][i]
    list2.append(stolb)
firs_element2 = list2[0]
for element in list2:
    if element != firs_element2:
        Flag=False
        break
    else:
        Flag=True
if Flag==True:
    print('YES')
else:
    print('NO')
