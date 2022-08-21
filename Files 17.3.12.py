#Статистика по файлу
#Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв латинского алфавита, слов и строк.
# Выведите три найденных числа в формате, приведенном в примере.

#Формат входных данных
#На вход программе ничего не подается.

#Формат выходных данных
#Программа должна вывести три найденных числа в формате, приведенном в примере.

#Примечание 1. Если бы файл file.txt содержал строки:

#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#то результатом было бы:

#Input file contains:
#108 letters
#20 words
#4 lines
#Примечание 2. Словом называется последовательность из непробельных символов. Например, строка

#abc a21 67pop    qwert bo7ok 83456
#содержит 66 слов: abc, a21, 67pop, qwert, bo7ok, 83456.

with open('file.txt') as file:
    file =[line.strip() for line in file.readlines()]
    num_of_lines=len(file)                                  #кол-во строк
    list1=[]
    сounter_of_letters=0
    for i in file:
        list1.append(i)
    list1 = ' '.join(list1)
    list1=list1.split()
    num_of_words=len(list1)
    for words in list1:
        for letters in words:
            if letters.isalpha():
                сounter_of_letters+=1
    print('Input file contains:')
    print(сounter_of_letters,'letters')
    print(num_of_words,'words')
    print(num_of_lines,'lines')