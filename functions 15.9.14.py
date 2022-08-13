#Отличники
#Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться,
# что в каждом классе есть хотя бы один отличник – ученик с оценкой 55 по контрольной работе.
# Напишите программу с использованием встроенных функций all(), any() для помощи Тимуру в проверке.

#Формат входных данных
#На вход программе подается натуральное число nn – количество классов. Затем для каждого класса вводится блок информации вида:

#натуральное число k – количество учеников в классе;
#далее вводится k строк вида: фамилия оценка.
#Формат выходных данных
#Программа должна вывести YES, если в каждом классе есть хотя бы один отличник, и NO в противном случае.

n = int(input())   #кол-во классов
list1=[]
for i in range(n):
    k = int(input())
    t=[]
    for j in range(k):
        string = input().split()
        t.append(string[-1])
        list1.append(t)
result=all(map(lambda x:True if '5' in x else False,list1))
if result==True:
    print('YES')
else:
    print('NO')