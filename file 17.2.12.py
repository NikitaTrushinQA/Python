#Предпоследняя строка
#На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его предпоследнюю строку.

#Формат входных данных
#На вход программе подается строка текста с именем существующего текстового файла.

#Формат выходных данных
#Программа должна вывести предпоследнюю строку указанного файла.

#Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

student_file = open(input())
result = student_file.readlines()
print(result[-2])
student_file.close()