#Математическое выражение
#На вход программе подается Decimal число dd. Напишите программу, которая вычисляет значение выражения:
#d.exp()+d.ln()+d.log10()+d.sqrt()
from decimal import *
d = Decimal(input())

result =d.exp()+d.ln()+d.log10()+d.sqrt()
print(result)