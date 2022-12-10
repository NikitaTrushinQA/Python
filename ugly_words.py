#ugly words
# n - количество букв в названии отдела
#s -строка  состоящая из латинских букв и пробелов
# b -длины n , состоящая из Y и B (цвета названия отдела)
#вывести количество некрасивыхслов в названии отдела
#input:
#27
#Algorithms and Data Structers
#BBBBBBBBBBBYYYYBBBBBBBBBB
#output:
#3

n = int(input())
s = input().split()
b = input()
counter = 0
mark = 0
for i in s:
    for j in range(mark + 1, mark + len(i)):
        if b[j] == b[j-1]:
            counter += 1
            break
    mark += len(i)
print(counter)