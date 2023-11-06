# Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
# которому соответствуют слова, записанные дважды подряд. Слова могут быть разделены одним или несколькими пробелами.
#
# Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W

regex = r'(\b\w+\b)[ ]+\b\1\b'

# Sample Input 1:
#
# One can can become a writer only  only if he is   is talented
# Sample Output 1:
#
# can can only  only is   is
# Sample Input 2:
#
# f fa fa
# Sample Output 2:
#
# fa fa
# Sample Input 3:
#
# tuk tak
# Sample Output 3: