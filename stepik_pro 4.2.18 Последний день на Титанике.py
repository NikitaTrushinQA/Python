#Последний день на Титанике
#Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник.
# В первом столбце указана единица, если пассажир выжил, и ноль в противном случае,
# во втором столбце записано полное имя пассажира, в третьем — пол, в четвертом — возраст:

#survived;name;sex;age
#0;Mr. Owen Harris Braund;male;22
#1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
#...
#Напишите программу, которая выводит имена выживших пассажиров, которым было менее
#18
#18 лет, каждое на отдельной строке. Причем сначала должны быть расположены имена всех пассажиров мужского пола,
# а затем — женского, имена же непосредственно в мужском и женском списках должны быть расположены в своем исходном порядке.

#Примечание 1. Разделителем в файле titanic.csv является точка с запятой, при этом кавычки не используются.






import csv

with open('titanic.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    d={}
    for row in rows:
        d[row['name']]=[row['survived'],row['sex'],row['age']]
    filtered_list = list(filter(lambda x: x[1][0] == '1' and float(x[1][2])<18, d.items())) #убираем погибших и меньше 18 лет
    filtered_list=filtered_list[::-1]
    result = sorted(filtered_list, key=lambda x: x[1][1])
    for names in result[::-1]:
        print(names[0])