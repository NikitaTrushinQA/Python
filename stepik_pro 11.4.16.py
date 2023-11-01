# Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
# которому соответствуют строки длины 45, удовлетворяющие следующим условиям:
#
# первые 40 символов являются либо латинскими буквами произвольного регистра, либо четными цифрами
# последние 5 символов являются либо нечетными цифрами, либо символами пробела

regex = r'^[a-zA-Z02468]{40}[13579\s]{5}'