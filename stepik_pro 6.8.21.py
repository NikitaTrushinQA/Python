# Для дополнительного заработка Тимур решил заняться продажей овощей.
# У него имеются данные о продажах за год, разделенные на четыре файла по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv.
# В каждом файле в первом столбце указывается название продукта, а в последующих — количество проданного продукта в килограммах за определенный месяц:
#
# продукт,январь,февраль,март
# Картофель,39,61,3
# Дайкон,51,96,83
# ...
# Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта, а значением — цена за килограмм в рублях:
#
# {
#    "Картофель": 53,
#    "Дайкон": 55,
# ...
# }
# Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.

import csv
from collections import defaultdict
import json

d = defaultdict(int)
for num in range(1,5):
    with open(f'quarter{num}.csv',encoding='UTF-8') as file:
        rows = list(csv.reader(file))[1:]
        for i in rows:
            d[i[0]]+= int(i[1])+int(i[2])+int(i[3])


with open ('prices.json',encoding='UTF-8') as file2:
    prices =json.load(file2)

result = 0
for i, j in zip(d,prices):
    result+=d[i]*prices[j]
print(result)