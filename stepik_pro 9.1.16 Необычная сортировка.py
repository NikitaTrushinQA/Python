# Необычная сортировка
# Дана строка, содержащая латинские буквы и цифры. Напишите программу, которая сортирует символы в строке согласно следующим правилам:
#
# все отсортированные строчные буквы стоят перед заглавными буквами
# все отсортированные заглавные буквы стоят перед цифрами
# все отсортированные нечетные цифры стоят перед отсортированными четными
# Формат входных данных
# На вход программе подается строка, содержащая латинские буквы и цифры.

# Sample Input 1:
#
# Sorting1234
# Sample Output 1:
#
# ginortS1324
# Sample Input 2:
#
# n0tEast3rEgg
# Sample Output 2:
#
# aggnrsttEE30
# Sample Input 3:
#
# 3DYrz34UXl
# Sample Output 3:
#
# lrzDUXY334

string = input()
result = sorted(string, key=lambda x: (x.isdigit() and not int(x) % 2, x.isdigit(), x.isupper(), x))
print(''.join(result))