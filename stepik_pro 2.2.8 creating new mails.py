#Корпоративная почта

#Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников
# в заранее подготовленном виде (латиницей с символом - между ними).
# Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

#Формат входных данных
#На вход программе в первой строке подается целое неотрицательное число n — количество выданных ящиков.
# В следующих n строках перечислены сами ящики в порядке выдачи, по одному на строке.
# На следующей строке задано целое неотрицательное число m — количество новых сотрудников,
# которым нужно раздать корпоративные ящики.
# Каждая из последующих m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

#Формат выходных данных
#Программа должна вывести почтовые ящики (mm строк) для новых сотрудников в том порядке, в котором они раздавались.

list_of_boxes = [input() for _ in range (int(input()))]
list_of_new_workers = [input() for _ in range (int(input()))]
for i in list_of_new_workers:                                      #
    n = 1
    name = i + '@beegeek.bzz'
    while name in list_of_boxes:
        name = i + str(n) + '@beegeek.bzz'
        n += 1
    print (name)
    list_of_boxes.append(name)




#Sample Input 1:

#6
#ivan-petrov@beegeek.bzz
#petr-ivanov@beegeek.bzz
#ivan-petrov1@beegeek.bzz
#ivan-ivanov@beegeek.bzz
#ivan-ivanov1@beegeek.bzz
#ivan-ivanov2@beegeek.bzz
#3
#ivan-ivanov
#petr-petrov
#petr-ivanov
#Sample Output 1:

#ivan-ivanov3@beegeek.bzz
#petr-petrov@beegeek.bzz
#petr-ivanov1@beegeek.bzz