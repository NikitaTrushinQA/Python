# Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
# которому соответствуют последовательности из 8 цифр.
# Причем последовательность может содержать символы дефиса - в качестве разделителей,
# только если они делят ее на группы по 2 цифры.

regex = r'\d{2}(-?)(\d{2}\1){2}\d{2}'

# Sample Input 1:
#
# Digits from 0 to 7: 01234567
# Sample Output 1:
#
# 01234567
# Sample Input 2:
#
# Digits from 1 to 8 by groups: 12-34-56-78
# Sample Output 2:
# 
# 12-34-56-78
# Sample Input 3:
#
# Digits from 1 to 8 by groups: 1234-5678
# Sample Output 3: