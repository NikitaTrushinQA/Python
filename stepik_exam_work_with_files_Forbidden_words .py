#Forbidden words
#На вход программе подается строка текста с именем текстового файла. Напишите программу,
# выводящую на экран содержимое этого файла,
# но с заменой всех запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).

#Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Гарантируется, что все слова в этом файле записаны в нижнем регистре.

#Формат входных данных
#На вход программе подается строка текста с именем существующего текстового файла,
# в котором необходимо заменить запрещенные слова звездочками.

#Формат выходных данных
#Программа должна вывести текст в соответствии с условием задачи.

#Примечание 1. Ваша программа должна заменить запрещенные слова,
# где бы они ни встречались, даже если они встречаются в середине другого слова.

#Примечание 2. Программа должна заменять запрещенные слова независимо от их регистра.
# Например, если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam,
# Exam, ExaM, EXAM и подобные должны быть заменены на ****.

#Примечание 3. Если бы файл forbidden_words.txt содержал слова:

#hello email python the exam wor is
#а файл в котором заменяются слова имел бы вид:

#Hello, world! Python IS the programming language of thE future. My EMAIL is....
#PYTHON is awesome!!!!
#то результатом будет:

#*****, ***ld! ****** ** *** programming language of *** future. My ***** **....
#****** ** awesome!!!!

name1 = input()  # data.txt
name2 = 'forbidden_words.txt'
with open(name2, 'r', encoding='utf-8') as forb:
    exp = forb.readlines()
    forbiden_words = exp[0].split(' ')

with open(name1, 'r+', encoding='utf-8') as file:
    file2 = file.readlines()
    stroka = ''
    for i in file2:
        stroka += i
    stroka_lower = stroka.lower()
    for w in forbiden_words:
        stroka_lower = stroka_lower.replace(w.lower(), '*' * len(w))
    result = ''
    for j in range(len(stroka_lower)):
        if stroka_lower[j] == '*':
            result += '*'
        elif stroka_lower[j] != '*' and stroka_lower[j] != stroka[j]:
            result += stroka[j]
        else:
            result += stroka_lower[j]
print(result)







