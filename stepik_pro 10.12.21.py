# Вам доступна функция password_gen(), которая возвращает генератор, порождающий все трехсимвольные строковые пароли в порядке возрастания,
# составленные из цифр от 00 до 99 включительно.
#
# Перепишите данную функцию с использованием функции product(), чтобы она выполняла ту же задачу.

from itertools import product
def password_gen():
    gen = product([str(i) for i in range(10)],repeat = 3)
    for i in gen:
        yield ''.join(i)


# Sample Input:
#
# passwords = password_gen()
#
# print(next(passwords))
# print(next(passwords))
# print(next(passwords))
# Sample Output:
#
# 000
# 001
# 002