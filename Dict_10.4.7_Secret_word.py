#Секретное слово
#Напишите программу для расшифровки секретного слова методом частотного анализа.

#Формат входных данных
#В первой строке задано зашифрованное слово. Во второй строке задано одно целое число n – количество букв в словаре.
# В следующих n строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.

#Формат выходных данных
#Программа должна вывести дешифрованное слово.

#Примечание. Гарантируется, что частоты букв не повторяются.
#Sample Input 1:
#*!*!*?
#3
#а: 3
#н: 2
#с: 1
#Sample Output 1:
#ананас
dict1 = {}
dict2 = {}     #словарь для дешифратора
slovo_basic =input()                  #вводим зашифрованное слово
slovo=list(slovo_basic)
for i in slovo:                           #заполняем словарь ключ-символ(буква) :значение - кол-во повторениц
    dict1[i]=dict1.get(i,0)+1
n = int(input())
for letters in range(n):                       #заполняем 2ой словарь-дешифратор
    value, key = input().split(': ')
    dict2[int(key)] = value
for letter in slovo_basic:
    print(dict2[dict1[letter]],end='')