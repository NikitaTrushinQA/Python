#Урок физики
#Даны по 10-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.

#Формат входных данных
#На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).

#Формат выходных данных
#Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, в соответствии с условием задачи.

#Примечание. Оценка ученика находится в диапазоне от 00 до 1010 включительно.

set1 = set(int(i) for i in input().split())
set2 = set(int(j) for j in input().split())
set3 = set(int(j) for j in input().split())
#print(set1)
#print(set2)
#print(set3)
set4=set3-(set1|set2)
result=sorted(set4,reverse=True)
print(*result)