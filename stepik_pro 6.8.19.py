# Функция scrabble()
# Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:
#
# symbols — набор символов
# word — слово
# Функция должна возвращать True, если из набора символов symbols можно составить слово word, или False в противном случае.
#
# Примечание 1. При проверке учитывается количество символов, которые нужны для составления слова, и не учитывается их регистр.

# Sample Input 1:
#
# print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# print(scrabble('begk', 'beegeek'))
# Sample Output 2:
# False

from collections import Counter


def scrabble(symbols, word):
    counter1 = Counter(symbols.lower())
    counter2 = Counter(word.lower())
    return counter2 <= counter1


