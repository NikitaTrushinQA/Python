#Уникальные символы 1
#Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

#Формат входных данных
#На вход программе в первой строке подается число nn – общее количество слов. Далее идут n- строк с словами.

#Формат выходных данных
#Программа должна вывести на отдельной строке количество уникальных символов для каждого слова.
#Sample Input 1:
#3
#Тимур
#Beegeek
#АнанАс
#Sample Output 1:
#5
#4
#3

n =int(input())
for i in range(n):
  print(len(set(input().lower())))