#Исправление дубликатов 🌶️
#На вход программе подается строка, содержащая строки-идентификаторы.
# Напишите программу, которая исправляет их так, чтобы в результирующей строке не было дубликатов.
# Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.

#Формат входных данных
#На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.

#Формат выходных данных
#Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.

#Sample Input 1:
#a b c a a d c
#Sample Output 1:
#a b c a_1 a_2 d c_1
#Sample Input 2:
#a b c
#Sample Output 2:
#a b c

stroka = input().split()
#print(stroka)
dict1={}
for i in stroka:
    dict1[i] = dict1.get(i, -1) + 1
    if dict1[i]>=1:                        #если встречается 1 или более раз
        print(i,'_',str(dict1[i]),sep='',end=' ')
    else:
        print(i,end=' ')