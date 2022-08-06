#Юный математик 🌶
#Дима учится в седьмом классе и сейчас они проходят обыкновенные дроби с натуральными числителем и знаменателем.
#Вчера на уроке математики Дима узнал, что дробь называется правильной,
#если ее числитель меньше знаменателя, и несократимой,
#если нет равной ей дроби с меньшими натуральными числителем и знаменателем.

#Дима очень любит математику, поэтому дома он долго экспериментировал,
# придумывая и решая разные задачки с правильными несократимыми дробями.
# Одну из этих задач Дима предлагает решить вам с помощью компьютера.

#На вход программе подается натуральное число n.
# Напишите программу, которая находит наибольшую правильную несократимую дробь с суммой числителя и знаменателя равной n.

#Формат входных данных
#На вход программе подается натуральное число n.

#Формат выходных данных
#Программа должна вывести ответ на задачу.

#Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель (НОД) двух чисел.
# Функция реализована в модуле math.

from fractions import Fraction as F
from math import*
result=[]
n = int(input())
for i in range(1,n):
    for j in range(n,1,-1):
        if i + j == n and gcd(i,j) == 1 and i<j:
            result.append(F(i,j))
print(max(result))