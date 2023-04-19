# Функция count_occurences()
# Реализуйте функцию count_occurences(), которая принимает два аргумента в следующем порядке:
#
# word — слово
# words — последовательность слов, разделенных пробелом
# Функция должна определять, сколько раз слово word встречается в последовательности words, и возвращать полученный результат.
#
# Примечание 1. Функция должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию count_occurences(), но не код, вызывающий ее.

# Sample Input 1:
#
# word = 'python'
# words = 'Python Conferences python training python events'
#
# print(count_occurences(word, words))
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# word = 'Java'
# words = 'Python C++ C# JavaScript Go Assembler'
#
# print(count_occurences(word, words))
# Sample Output 2:
#0

from collections import Counter

def count_occurences(word,words):
    couter = Counter(words.lower().split(' '))
    return couter[word.lower()]