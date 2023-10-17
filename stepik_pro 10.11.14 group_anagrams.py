# Функция group_anagrams()
# Анаграммы — это слова, которые состоят из одинаковых букв. Например:
#
# адаптер — петарда
# адресочек — середочка
# азбука — базука
# аистенок — осетинка

# Реализуйте функцию group_anagrams(), которая принимает один аргумент:
# words — список слов

# Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами, и возвращать список полученных кортежей.
#
# Примечание 1. Порядок кортежей в возвращаемом функцией списке, а также порядок элементов в этих кортежах, не важен.



from itertools import groupby

def group_anagrams(words):
    func = lambda x :sum(ord(i) for i in x)
    words = sorted(words,key=func)
    result = [tuple(j) for i,j in groupby(words,key=func)]
    return result

groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])

print(*groups)

# Sample Input 1:
# groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
# print(*groups)
# Sample Output 1:
# ('boko', 'book') ('evil', 'levi', 'live') ('afther', 'father')
#
# Sample Input 2:
# groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])
# print(*groups)
# Sample Output 2:
# ('beegeek',) ('book',) ('evil',) ('father',) ('stepik',)
#
# Sample Input 3:
# groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])
# print(*groups)
# Sample Output 3:
# ('крона', 'норка') ('сеточка', 'тесачок', 'стоечка') ('лучик', 'чулки')

