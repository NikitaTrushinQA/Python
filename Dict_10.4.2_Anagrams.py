#Анаграммы 1
#Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание).
# Например, английские слова evil и live – это анаграммы.

#На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

#Формат входных данных
#На вход программе подаются два слова, каждое на отдельной строке.

#Формат выходных данных
#Программа должна вывести YES если слова являются анаграммами и NO в противном случае.
#Тестовые данные 🟢
#Sample Input 1:
#thing
#night
#Sample Output 1:
#YES

spisok = []
dict1 = {}
dict2 = {}
for i in range(2):
    spisok.append(input())
#print(spisok)
for letters1 in spisok[0]:
    dict1[letters1]=dict1.get(letters1,0)+1
#print(dict1)
for letters2 in spisok[1]:
    dict2[letters2]=dict2.get(letters2,0)+1
#print(dict2)
if dict1==dict2:
    print('YES')
else:
    print('NO')