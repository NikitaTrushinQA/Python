# Дополните приведенный ниже код, чтобы в переменной infinite_love содержался итератор,
# бесконечно генерирующий единственное значение — строку i love beegeek!.

infinite_love = iter(lambda :'i love beegeek!', -1)

# Sample Input 1:
#
# print(next(infinite_love))
# Sample Output 1:
#
# i love beegeek!
# Sample Input 2:
#
# print(next(infinite_love))
# print(next(infinite_love))
# print(next(infinite_love))
# Sample Output 2:
#
# i love beegeek!
# i love beegeek!
# i love beegeek!