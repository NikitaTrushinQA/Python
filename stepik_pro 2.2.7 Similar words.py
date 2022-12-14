#Схожие слова
#Напишите программу, которая находит все схожие слова для заданного слова. Слова называются схожими,
# если имеют одинаковое количество и расположение гласных букв. При этом сами гласные могут различаться.

#Формат входных данных
#На вход программе подается одно слово, записанное в первой строке, затем натуральное число nn — количество слов для сравнения и nn строк со словами.

#Формат выходных данных
#Программа должна вывести все схожие слова для заданного слова, сохранив их исходный порядок следования.

#Примечание 1. После последней гласной в начальном и проверяемом слове может быть любое количество согласных.

#Примечание 2. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и 21
# согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).
#Sample Input 1:

#машина
#8
#сеть
#машинист
#дорога
#урок
#работа
#аксиома
#железо
#ветеран
#Sample Output 1:

#машинист
#дорога
#работа
#железо
#ветеран


word = input()
list1 = []
for i in range(len(word)):
    if word[i] in 'ауоыиэяюёе':
        list1.append(i)
n = int(input())
for j in range(n):
    word2 = input()
    list2 = []
    for k in range(len(word2)):
        if word2[k] in 'ауоыиэяюёе':
            list2.append(k)
    if list1 == list2:
        print(word2)