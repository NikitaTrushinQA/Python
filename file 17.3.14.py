#Необычные страны
#Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом табуляции '\t'.

#Напишите программу выводящую все страны, название которых начинается с буквы 'G', численность населения которых больше чем 500 \, 000500000 человек, не меняя их порядок.

#Формат входных данных
#На вход программе ничего не подается.

#Формат выходных данных
#Программа должна вывести названия стран, удовлетворяющие условиям задачи, каждое на отдельное строке.

with open('population.txt') as file:
    file =[line.strip().split('\t') for line in file.readlines()]
    result=list(filter(lambda x: x[0][0] == 'G' and int(x[-1]) > 500_000,file))
    #print(result)

    for i in result:
        print(i[0])