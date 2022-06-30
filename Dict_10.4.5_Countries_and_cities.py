#Страны и города
#На вход программе подается список стран и городов каждой страны.
#Затем даны названия городов. Напишите программу, которая для каждого города выводит, в какой стране он находится.

#Формат входных данных
#Программа получает на вход количество стран n.
# Далее идет n строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число m, далее идут m запросов — названия каких-то m городов, из перечисленных выше.

#Формат выходных данных
#Программа должна вывести название страны, в которой находится данный город в соответствии с примером.

#Тестовые данные
#Sample Input:
#2
#Германия Берлин Мюнхен Гамбург Дортмунд
#Нидерланды Амстердам Гаага Роттердам Алкмар
#4
#Амстердам
#Алкмар
#Гамбург
#Гаага
#Sample Output:
#Нидерланды
#Нидерланды
#Германия
#Нидерланды

dict1 = {}
spisok = []
n = int(input())
for i in range(n):
     a = input().split()  # отделяем наши будущие ключи и значения в списке
     dict1[a[0]] = a[1::]
#print(dict1)
m = int(input())                #вводим кол-во городов
for k in range(m):
    gorod = input()               #вводим город
    for key, value in (dict1.items()):
        if gorod in value:
            print(key)

