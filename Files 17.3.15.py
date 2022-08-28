#CSV-файл
#Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей.

#Формат входных данных
#На вход программе ничего не подается.

#Формат выходных данных
#Программа должна содержать реализованную функцию read_csv.

#Примечание 1. Вызывать функцию read_csv не нужно.

#Примечание 2. Функция read_csv не должна принимать аргументов.

#Примечание 2. Подробнее прочитать про CSV-файлы можно тут.

#Примечание 3. Считайте, что все ключи и значения по этим ключам в результирующем словаре имеют строковый тип (str).

#Примечание 4. Содержание файла data.csv:
#policyID,statecode,county,eq_site_limit,hu_site_limit,fl_site_limit,fr_site_limit,tiv_2011,tiv_2012,eq_site_deductible,hu_site_deductible,fl_site_deductible,fr_site_deductible,point_latitude,point_longitude,line,construction,point_granularity
#119736,FL,CLAY COUNTY,498960,498960,498960,498960,498960,792148.9,0,9979.2,0,0,30.102261,-81.711777,Residential,Masonry,1
#448094,FL,CLAY COUNTY,1322376.3,1322376.3,1322376.3,1322376.3,1322376.3,1438163.57,0,0,0,0,30.063936,-81.707664,Residential,Masonry,3
#206893,FL,CLAY COUNTY,190724.4,190724.4,190724.4,190724.4,190724.4,192476.78,0,0,0,0,30.089579,-81.700455,Residential,Wood,1
#333743,FL,CLAY COUNTY,0,79520.76,0,0,79520.76,86854.48,0,0,0,0,30.063236,-81.707703,Residential,Wood,3
#172534,FL,CLAY COUNTY,0,254281.5,0,254281.5,254281.5,246144.49,0,0,0,0,30.060614,-81.702675,Residential,Wood,1
#785275,FL,CLAY COUNTY,0,515035.62,0,0,515035.62,884419.17,0,0,0,0,30.063236,-81.707703,Residential,Masonry,3
#995932,FL,CLAY COUNTY,0,19260000,0,0,19260000,20610000,0,0,0,0,30.102226,-81.713882,Commercial,Reinforced Concrete,1
#223488,FL,CLAY COUNTY,328500,328500,328500,328500,328500,348374.25,0,16425,0,0,30.102217,-81.707146,Residential,Wood,1
#433512,FL,CLAY COUNTY,315000,315000,315000,315000,315000,265821.57,0,15750,0,0,30.118774,-81.704613,Residential,Wood,1
#142071,FL,CLAY COUNTY,705600,705600,705600,705600,705600,1010842.56,14112,35280,0,0,30.100628,-81.703751,Residential,Masonry,1


#Примечание 5. Если бы файл data.csv содержал информацию

#name,address,age
#George,4312 Abbey Road,22
#John,54 Love Ave,21
#то вызов функции read_csv() вернул бы список:
#[{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'}, {'name': 'John', 'address': '54 Love Ave', 'age': '21'}]

def read_csv():
    with open('data.csv') as file:
        result=[]
        file = [line.strip().split('\t') for line in file.readlines()]
        keys=','.join(file[0]).split(',')
        values=file[1::]
        new_values=[]
        for i in values:
            i=','.join(i).split(',')
            new_values.append(i)
        #print('keys=',keys)
        #print('values=',values)
        #print('new_values=',new_values)
        for i in range(10):
            dict1={}
            dict1=dict(zip(keys, new_values[i]))
            result.append(dict1)
        return(result)

read_csv()