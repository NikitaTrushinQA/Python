#Загадка от Жака Фреско ️
#Однажды Жака Фреско спросили:
#"Если ты такой умный, почему не богатый?"
#Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:
#"Были разноцветные козлы. Сколько?"
#"Сколько чего?"
#"Сколько из них составляет более 7% от общего количества козлов?"

#Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех возможных цветов козлов.
#Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.

#Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от Жака Фреско.

#Формат входных данных
#На вход программе ничего не подается.

#Формат выходных данных
#Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов, которые удовлетворяют условию загадки Жака Фреско.

#Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

#Примечание 2. Если бы файл goats.txt содержал строки:

#COLOURS
#Pink goat
#Green goat
#Black goat
#GOATS
#Pink goat
#Pink goat
#Black goat
#Pink goat
#Pink goat
#Black goat
#Green goat
#Pink goat
#Black goat
#Black goat
#Pink goat
#Pink goat
#Black goat
#Black goat
#Pink goat
#то файл answer.txt имел бы вид:

#Black goat
#Pink goat

from collections import Counter
with open('goats.txt') as inp, open('answer.txt', 'w') as out:
    inp = [line.strip() for line in inp.readlines()]
    dict1= dict(Counter(inp))
    total= len(inp)-len(dict1)
    del dict1['COLOURS']
    del dict1['GOATS']
    counter = 0
    for key, value in dict1.items():
        if int(((value - 1) / total) * 100) > 7:
            print(key,file=out)