#Функция spell()
#Реализуйте функцию spell(), которая принимает произвольное количество позиционных аргументов-слов и возвращает словарь, ключи которого — первые буквы слов,
# а значения — максимальные длины слов на эту букву.

#Примечание 1. Если в функцию не передается ни одного аргумента, функция должна возвращать пустой словарь.

#Примечание 2. Функция должна игнорировать регистр слов, при этом в результирующий словарь должны попасть именно буквы в нижнем регистре.

def spell(*words):
    result_dict = dict()
    new_words = []
    for word in words:
        new_words.append(word.lower())
    if len(new_words) > 0:
        result_dict[new_words[0][0]] = len(new_words[0])
        for i in range(1, len(words)):
            if new_words[i][0] in result_dict and len(new_words[i]) > result_dict[new_words[i][0]]:
                result_dict[new_words[i][0]] = len(new_words[i])
            elif new_words[i][0] not in result_dict:
                result_dict[new_words[i][0]] = len(new_words[i])
        return result_dict
    return result_dict
