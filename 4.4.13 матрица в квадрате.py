#Формат входных данных
#На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

#Формат выходных данных
#Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

#Примечание. Элементы диагоналей также учитываются.
# *  -показана часть квадрата
#  *o*
#  ***
#  *o*


n =int(input())
matrix =   [[int(i) for i in input().split()] for j in range(n)]
result=-1000
for i in range(n):
    for j in range(n):
        if  ((i>=j) and (i<=n-1-j)) or ((i<=j) and (i>=n-1-j)):
            if matrix[i][j]> result:
                result=matrix[i][j]
print(result)