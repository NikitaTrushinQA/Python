#Функция filter_anagrams()
#Анаграммы — это слова, которые состоят из одинаковых букв. Например:

#адаптер — петарда
#адресочек — середочка
#азбука — базука
#аистенок — осетинка
#Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:

#word — слово в нижнем регистре
#words — список слов в нижнем регистре
#Функция должна возвращать список, элементами которого являются слова из списка words,
# которые представляют анаграмму слова word. Если список words пуст или не содержит анаграмм,
# функция должна вернуть пустой список.

#Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке.

#Примечание 2. Считайте, что слово является анаграммой самого себя.

def filter_anagrams(word,anagrams):
    result = []
    dict1 = dict()      #словарь для букв в слове word
    dict2 = dict()      #словарь для букв в списке anagrams
    for i in word:
        dict1[i] = dict1.get(i,0)+1
    sorted_dict1 = dict(sorted(dict1.items()))
    for j in anagrams:
        for h in j:
            dict2[h] = dict2.get(h,0)+1
        sorted_dict2 = dict(sorted(dict2.items()))
        if sorted_dict1 == sorted_dict2:
            result.append(j)
        dict2={}
    return result

#или
#def filter_anagrams(word, anagrams):
    #return [i for i in anagrams if sorted(list(i)) == sorted(list(word))]

