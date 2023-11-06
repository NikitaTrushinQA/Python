# Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
# которому соответствуют слова, содержащие повторяющиеся буквы.

regex = r'\b\w*(\w)\w*\1\w*\b'

# Sample Input 1:
#
# I have one apple, one banana and one strawberry
# Sample Output 1:
#
# apple banana strawberry
# Sample Input 2:
#
# Priveeeet my dear friend
# Sample Output 2:
#
# Priveeeet
# Sample Input 3:
#
# fuisopf gheos, geisslp
# Sample Output 3:
#
# fuisopf geisslp