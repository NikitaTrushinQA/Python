#Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.

from decimal import *
num = Decimal(input())
#print(num)
if abs(num)<1:
    print(max(num.as_tuple().digits)+0)
else:
    print(max(num.as_tuple().digits)+min(num.as_tuple().digits))