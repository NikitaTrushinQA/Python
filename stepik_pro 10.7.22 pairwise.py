# Функция pairwise()
# Реализуйте генераторную функцию, которая принимает один аргумент:
#
# iterable — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность кортежей,
# каждый из которых содержит очередной элемент итерируемого объекта iterable, а также следующий за ним элемент:
#
# (<очередной элемент>, <следующий элемент>)
# Для последнего элемента следующим считается значение None.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
#
# Sample Input 1:
#
# numbers = [1, 2, 3, 4, 5]
#
# print(*pairwise(numbers))
# Sample Output 1:
#
# (1, 2) (2, 3) (3, 4) (4, 5) (5, None)
# Sample Input 2:
#
# iterator = iter('stepik')
#
# print(*pairwise(iterator))
# Sample Output 2:
#
# ('s', 't') ('t', 'e') ('e', 'p') ('p', 'i') ('i', 'k') ('k', None)


def pairwise(iterable):
    if iterable:
        iterator = iter(iterable)
        prev = next(iterator)
        for element in iterator:
            yield prev, element
            prev = element
        yield (prev, None)
    else:
        return []

print(list(pairwise([])))
