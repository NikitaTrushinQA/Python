#Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам,
#складывая значения по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях.
# Результирующий словарь необходимо присвоить переменной result.

#Примечание. Выводить содержимое словаря result не нужно.

#Приведенный код:
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
#дополнение:
result=dict1.copy()
print(result)
for i in result:
    result[i]=result.get(i,0)+dict2[i]


#print(result)
#check = {'a': 400, 'b': 400, 'c': 312, 'd': 445, 'e': 98, 'f': 90, 'm': 230, 'p': 123, 'q': 34, 't': 853, 'w': 111, 'z': 999}