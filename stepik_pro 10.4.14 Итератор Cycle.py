# Итератор Cycle
# Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:
#
# iterable — итерируемый объект
# Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого объекта iterable.
#
# Примечание 1. Гарантируется, что итерируемый объект, передаваемый в конструктор класса, не является множеством и итератором.
#
# Примечание 2. Элементы итерируемого объекта, генерируемые итератором, должны располагаться в своем изначальном порядке.

class Cycle:
    def __init__(self,iterable):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.index += 1
            return self.iterable[self.index]
        except IndexError:
            self.index = 0
            return self.iterable[self.index]

cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
