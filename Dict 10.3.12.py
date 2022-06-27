#Дополните приведенный код так, чтобы в переменной result хранился словарь,
# в котором для каждого символа строки text будет подсчитано количество его вхождений.
#Примечание. Выводить содержимое словаря result не нужно.
#Приведенный код:

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
#дополнение:
for num in text:
    result[num]=result.get(num,0)+1

