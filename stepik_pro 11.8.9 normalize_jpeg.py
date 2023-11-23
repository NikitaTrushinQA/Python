# Реализуйте функцию normalize_jpeg(), которая принимает один аргумент:
#
# filename — название файла, имеющее расширение jpeg или jpg, которое может быть записано буквами произвольного регистра
# Функция должна возвращать новое название файла с нормализованным расширением — jpg.

import re
def normalize_jpeg(filename):
    result = re.sub(r'(\.\w+)$',r'.jpg',filename)
    return result

# Sample Input 1:
#
# print(normalize_jpeg('stepik.jPeG'))
# Sample Output 1:
#
# stepik.jpg
# Sample Input 2:
#
# print(normalize_jpeg('mountains.JPG'))
# Sample Output 2:
#
# mountains.jpg
# Sample Input 3:
#
# print(normalize_jpeg('windows11.jpg'))
# Sample Output 3:
#
# windows11.jpg
