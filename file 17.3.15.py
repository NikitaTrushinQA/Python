#CSV-файл
#Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из этого файла.
# Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей.

#Формат входных данных
#На вход программе ничего не подается.

#Формат выходных данных
#Программа должна содержать реализованную функцию read_csv.

#Примечание 1. Вызывать функцию read_csv не нужно.

#Примечание 2. Функция read_csv не должна принимать аргументов.

#Примечание 3. Если бы файл data.csv содержал информацию

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
        for i in range(10):
            dict1={}
            dict1=dict(zip(keys, new_values[i]))
            result.append(dict1)
        return(result)

read_csv()



#def read_csv():
    #with open('data.csv') as file:
       # file = tuple(map(lambda x: x.strip().split(','), file))
       # return [dict(zip(file[0], i)) for i in file[1:]]