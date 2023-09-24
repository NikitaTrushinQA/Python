# Функция filter_names()
# Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:
#
# names — список имен
# ignore_char — одиночный символ
# max_names — натуральное число
# Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые
#
# начинаются на ignore_char (в любом регистре)
# содержат хотя бы одну цифру
# Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из данного списка.
#
# Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

def filter_names(names,ignore_char,max_names):
    counter = 0
    begin = (i for i in names if i[0].lower()!=ignore_char.lower() and i.isalpha())
    if max_names>len(data):
        yield from begin

    else:
        counter+=1
        try:
            if counter<=max_names:
                for i in begin






data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))

#Timur Arthur Arina