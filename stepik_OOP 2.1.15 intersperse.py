# Функция intersperse()
#
# Реализуйте генераторную функцию intersperse(), которая принимает два аргумента в следующем порядке:
#
#     iterable — итерируемый объект
#     delimiter — значение-разделитель
#
# Функция должна возвращать генератор, порождающий последовательность из элементов итерируемого объекта iterable,
# между которыми располагается значение-разделитель delimiter.
#
# Примечание 1. Рассмотрим первый тест, в котором в качестве итерируемого объекта передается список чисел от 1 до 3,
# а в качестве значения-разделителя — 0. Порождаемая генератором последовательность состоит из чисел 1, 2 и 3, между которыми располагается число 0:
#
# 1 0 2 0 3

def intersperse(iterable, delimiter):
    flag = True
    for item in iterable:
        if not flag:
            yield delimiter
        flag = False
        yield item




# Sample Input 1:
#
# print(*intersperse([1, 2, 3], 0))
#
# Sample Output 1:
#
# 1 0 2 0 3
#
# Sample Input 2:
#
# inter = intersperse('beegeek', '!')
# print(next(inter))
# print(next(inter))
# print(*inter)
#
# Sample Output 2:
#
# b
# !
# e ! e ! g ! e ! e ! k
#
# Sample Input 3:
#
# print(*intersperse('A', '...'))
#
# Sample Output 3:
#
# A

