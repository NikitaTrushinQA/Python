#Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько,
# должно быть выведено то, что меньше в лексикографическом порядке.

#Приведенный код:
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry' \
    ' barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange ' \
    'lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry ' \
    'apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon' \
    ' pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

#Дополнение:
stroka=s.split()
dict1={}                                               #словарь-счетчик
dict2={}                                               #словарь для слов с максимально повторяющимися значениями
for i in stroka:
    dict1[i]=dict1.get(i,0)+1
max=max(dict1.values())
for key,value in dict1.items(): # цикл для перебора первого словаря и наполнения второго словаря парами с максимальным значением
    if value==max:
        dict2[key]=dict2.get(key,value)
result=min(dict2)
print(result)


