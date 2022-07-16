#Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter,
# где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).

#Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

import random
import string
def generate_index():
    list_Numbers =[]
    for i in range(100):
        list_Numbers.append(str(i))
    list1 = []        #список для первой части индекса включая '_'
    list2 = []        #список для 2ой части индекса ( после '_')
    for j in range(2):
        list1.append(str(random.choice(string.ascii_uppercase)))
    list1.append(str(random.choice(list_Numbers)))
    list1.append('_')
    list2.append(str(random.choice(list_Numbers)))
    for k in range(2):
        list2.append(str(random.choice(string.ascii_uppercase)))
    mail_index = ''.join(list1+list2)
    return mail_index
