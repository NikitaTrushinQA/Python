#Нумерация строк
#Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел. Нумерация строк должна начинаться с 11.

#Формат входных данных
#На вход программе ничего не подается.

#Формат выходных данных
#Программа должна создать файл с именем output.txt и записать в него пронумерованные строки файла input.txt.

#Примечание . Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

#Примечание . Используйте встроенную функцию enumerate().

#Примечание . Если бы файл input.txt содержал строки:

#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#то файл output.txt имел бы вид:

#1) Beautiful is better than ugly.
#2) Explicit is better than implicit.
#3) Simple is better than complex.
#4) Complex is better than complicated.

#Примечание . файл input.txt содержит строки:
#abcd
#xcnvmnvkje
#32432423
#sdflsdjkn34r43
#345349854395#$%$#
#jksdfkjsdfkjsd
#lwerjlwerlkwe
#jwfhjkwehkjwefkjwebfjkwe
#djdddddddddddddddddddddddddddddddd
#3249835438594390583490583490853490582349058340
#sdfsjkldflksdjaflkjsdflkjsdlfkjsdlfjsldfsldkfjlsdkfjls

with open('input.txt','r') as file1:
    file1 = [line.strip() for line in file1.readlines()]
    #print(file1)
with open('output.txt', 'w') as file2:
    for pair in enumerate(file1,1):
        print(*pair, file=file2,sep=') ')