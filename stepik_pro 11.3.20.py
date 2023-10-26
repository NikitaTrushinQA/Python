# Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
# которому соответствуют почтовые индексы Великобритании, удовлетворяющие следующим условиям:
#
# почтовый индекс начинается с одной или двух заглавных латинских букв, за которыми следует одна цифра.
# После цифры может следовать один необязательный символ — цифра или заглавная латинская буква
# далее через пробел указываются одна цифра и любые две заглавные латинские буквы, кроме C, I, K, M, O, V

regex = r'[A-Z]{1,2}\d[0-9|A-Z]?\s\d[ABD-HJLNP-UW-Z]{2}'

# Sample Input 1:
#
# Our postcodes. Arthur: NW11 8AB, Timur: P01 3AX, Anri: H7Z9T4 Dima: N16 6PS
# Sample Output 1:
#
# NW11 8AB P01 3AX N16 6PS
# Sample Input 2:
#
# my postcode is: 1 1PR, but it's not correct, my another postcode P0Z 9AU, it's correct, Artur's postcode CI0 0GG, it's correct, Timur's postcode CIK7O 8JH, it's not correct
# Sample Output 2:
#
# P0Z 9AU CI0 0GG IK7O 8JH
