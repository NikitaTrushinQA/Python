# Функция palindromes()
# Реализуйте генераторную функцию palindromes(), которая не принимает никаких аргументов.
#
# Функция должна возвращать генератор, порождающий бесконечную последовательность натуральных чисел-палиндромов.
#
# Примечание 1. Число-палиндром — число, которое читается одинаково как справа налево, так и слева направо.

def palindromes():
    n=0
    while True:
        n+=1
        if str(n)==str(n)[::-1]:
            yield n

# Sample Input 1:
#
# generator = palindromes()
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# Sample Output 1:
#
# 1
# 2
# 3
# Sample Input 2:
#
# generator = palindromes()
# numbers = [next(generator) for _ in range(30)]
#
# print(*numbers)
# Sample Output 2:
#
# 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212