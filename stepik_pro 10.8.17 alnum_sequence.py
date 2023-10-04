# alnum_sequence
# Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.
#
# Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность натуральных чисел и заглавных латинских букв:

import string

from itertools import cycle

def alnum_sequence():
    letters = string.ascii_uppercase
    gen = cycle(elem for tuple in zip(range(1,27),letters) for elem in tuple)
    yield from gen


# Sample Input 1:
#
# alnum = alnum_sequence()
#
# print(*(next(alnum) for _ in range(55)))
# Sample Output 1:
#
# 1 A 2 B 3 C 4 D 5 E 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X 25 Y 26 Z 1 A 2
# Sample Input 2:
#
# alnum = alnum_sequence()
#
# print(*(next(alnum) for _ in range(100)))
# Sample Output 2:
#
# 1 A 2 B 3 C 4 D 5 E 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X 25 Y 26 Z 1 A 2 B 3 C 4 D 5 E
# 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X