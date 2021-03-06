#Самое редкое слово 🌶️
#На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра.
#Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

#Формат входных данных
#На вход программе подается строка текста.

#Формат выходных данных
#Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

#Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.

#Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, которые нужно игнорировать.
# Других символов в тексте нет.

#Sample Input 2:

#home sweet home sweet.
#Sample Output 2:

#home

import re
stroka = input()
stroka2 = re.sub("[.,;:-?-!()]",'',stroka.lower()) #убираем  .,;:-?-!()
stroka2=stroka2.split()
dict1={}                                               #словарь-счетчик
dict2={}                                               #словарь для слов с максимально повторяющимися значениями
#print('stroka2=',stroka2)
for i in stroka2:                                     #проходим по строке и записываем в словарь с увеличением value
    dict1[i]=dict1.get(i,0)+1
#print('dict1',dict1)
minimum=min(dict1.values())
for key,value in dict1.items(): # цикл для перебора первого словаря и наполнения второго словаря парами с минимальными значениями
    if value==minimum:
        dict2[key]=dict2.get(key,value)
result=min(dict2)
print(result)

