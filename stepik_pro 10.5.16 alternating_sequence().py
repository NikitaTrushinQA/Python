# Функция alternating_sequence()
# Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:
#
# count — натуральное число, по умолчанию имеет значение None
# Если count имеет значение None, функция должна возвращать генератор, порождающий бесконечный знакочередующийся ряд натуральных чисел.
#
# Если count имеет в качестве значения натуральное число, функция должна возвращать генератор,
# порождающий первые count чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий исключение StopIteration.
#
# Примечание 1. Знакочередующийся ряд натуральных чисел имеет вид:
# 1, -2, 3, -4, 5, -6, 7, -8, 9, -10, ...


def alternating_sequence(count=None):
    n = 1
    index = 0
    if count==None:
        while True:
            yield n
            if n%2:
                n=(-1)*(n+1)
            else:
                n = -1 * (n - 1)

    else:
        while index!= count:
            for i in range(1,count+1):
                if i % 2:
                    yield i
                else:
                    yield i*(-1)
                index+=1
        return 55



# Sample Input 1:
#
# generator = alternating_sequence()
#
# print(next(generator))
# print(next(generator))
# Sample Output 1:
#
# 1
# -2
# Sample Input 2:
#
# generator = alternating_sequence(10)
#
# print(*generator)
# Sample Output 2:
#
# 1 -2 3 -4 5 -6 7 -8 9 -10
