#Wi-Fi Москвы
#Вам доступен файл wifi.csv, который содержит данные о городском Wi-Fi Москвы.
#В первом столбце записано название округа, во втором — название района, в третьем — адрес,
# в четвертом — количество точек доступа по этому адресу:

#adm_area;district;location;number_of_access_points
#Центральный административный округ;район Якиманка;город Москва, улица Серафимовича, дом 5/16;5
#Центральный административный округ;район Якиманка;город Москва, Болотная набережная, дом 11, строение 1;2
#...
#Напишите программу, которая определяет количество точек доступа в каждом районе Москвы и выводит названия всех районов,
# для каждого указывая соответствующее количество точек доступа, каждое на отдельной строке, в следующем формате:

#<название района>: <количество точек доступа>
#Названия районов должны быть расположены в порядке убывания количества точек доступа,
# при совпадении количества точек доступа — в лексикографическом порядке.

#Примечание 1. Разделителем в файле wifi.csv является точка с запятой, при этом кавычки не используются.

#Примечание 2. При сортировке названия районов должны быть использованы именно в том виде,
# в котором они указаны в исходном файле. Выполнять какие-либо дополнительные преобразования не нужно.

import csv

with open('wifi.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    d={}
    for row in rows:
        d[row['district']]=d.setdefault(row['district'], 0)+int(row['number_of_access_points'])
    print('d=',d)
    result=sorted(d.items(), key= lambda x:(-x[1], x[0]))
    print('result=',result)
    for i in result:
        print(f'{i[0]}: {i[1]}')
