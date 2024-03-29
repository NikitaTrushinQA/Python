#Более одного
#Дана последовательность неотрицательных целых чисел. Напишите программу, которая выводит те числа,
# которые встречаются в данной последовательности более одного раза.

#Формат входных данных
#На вход программе подается строка, содержащая целые неотрицательные числа, разделенные пробелом.

#Формат выходных данных
#Программа должна вывести те числа, которые встречаются в данной строке более одного раза, разделяя их пробелом.
# Числа должны быть расположены в порядке возрастания и не должны повторяться.

#Примечание 1. Если повторяющихся чисел в исходной строке нет, программа ничего не должна выводить.

#Sample Input 1:

#4 8 0 3 4 2 0 3
#Sample Output 1:

#0 3 4

numbers = input().split(' ')
d = dict()
for i in numbers:
    d[i]= d.setdefault(i,0) + 1
result =[]
for key in d:
    if d[key] > 1:
        result.append(int(key))
if result != []:
    print(*(sorted(result)))