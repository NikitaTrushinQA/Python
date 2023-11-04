# Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
# которому соответствуют последовательности символов длины 6, удовлетворяющие следующим условиям:
#
# первый символ — строчная латинская буква
# второй символ — цифра, любая буква в произвольном регистре или символ нижнего подчеркивания
# третий символ — заглавная латинская буква
# четвертый символ должен совпадать с первым символом
# пятый символ должен совпадать со вторым символом
# шестой символ должен совпадать с третьим символом

regex = r'([a-z])(\w)([A-Z])\1\2\3'

# Sample Input 1:
# Hello, User211, your verification number: z5Az5A

# Sample Output 1:
# z5Az5A

# Sample Input 2:
# Let's check case: 40H40H (not correct), 40Ha0H (not correct),  a_Ab_A (not correct), abCAbc (not correct), a0Aa0A (correct)
# Sample Output 2:
# a0Aa0A

# Sample Input 3:
# j1Pj0p, jYOjQO, v-Ev-E, lsXl2X, m.Wm.W, m.Zm2Z, h0Nh0N
# Sample Output 3:
# h0Nh0N