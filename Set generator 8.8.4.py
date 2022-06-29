#Используя генератор множеств, дополните приведенный код,
#так чтобы получить множество, содержащее первую букву каждого слова (в нижнем регистре) списка words.
#Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.

words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
myset={i[0].lower() for i in words}
print(*sorted(myset))
