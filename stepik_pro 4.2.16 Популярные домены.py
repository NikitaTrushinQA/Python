#Реализуйте функцию csv_columns(), которая принимает один аргумент:

#filename — название csv файла, например, data.csv
#Функция должна возвращать словарь, в котором ключом является название столбца файла filename, а значением — список элементов этого столбца.

#Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем является запятая, при этом кавычки не используются.

#Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.

#Примечание 3. Например, если бы файл exam.csv имел вид:

#name,grade
#Timur,5
#Arthur,4
#Anri,5
#то следующий вызов функции csv_columns():

#csv_columns('exam.csv')
#должен был бы вернуть:

#{'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}
#Примечание 4. Ключи в словаре, а также элементы в списках должны располагаться в своем исходном порядке.

import csv
with open('data.csv', 'r', encoding='utf-8') as file1, open('domain_usage.csv','w',encoding='utf-8',newline='') as file2:
    rows =list(csv.reader(file1, delimiter='@'))
    dic={}
    rows.pop(0)
    for i in rows:
        dic[i[1]]=dic.setdefault(i[1],0)+1
    new_list=list(dic.items())
    columns=['domain','count']
    writer = csv.writer(file2)
    writer.writerow(columns)
    for j in sorted(new_list, key=lambda x: (x[1],x[0])):
        writer.writerow(j)
