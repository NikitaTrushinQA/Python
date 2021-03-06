#Суммы четвертей
#Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
#Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.

#Формат входных данных
#На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.

#Формат выходных данных
#Программа должна вывести текст в соответствии с условием задачи.

#Примечание. Элементы диагоналей не учитываются.




n =int(input())
matrix =   [[int(i) for i in input().split()] for j in range(n)]
max_verx=0
max_prav=0
max_niz=0
max_levo=0
for i in range(n):
    for j in range(n):
        if i<j and i<n-1-j:
            max_verx+=matrix[i][j]
        if i<j and i>n-1-j:
            max_prav+=matrix[i][j]
        if i>j and i>n-1-j:
            max_niz+=matrix[i][j]
        if i>j and i<n-1-j:
             max_levo+=matrix[i][j]
print('Верхняя четверть:',max_verx)
print('Правая четверть:',max_prav)
print('Нижняя четверть:',max_niz)
print('Левая четверть:',max_levo)