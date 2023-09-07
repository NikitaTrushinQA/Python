# Итератор Repeater
# Реализуйте класс Repeater, порождающий итераторы, конструктор которого принимает один аргумент:
#
# obj — произвольный объект
# Итератор класса Repeater должен бесконечно генерировать единственное значение — obj.

class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


bee = Repeater('bee')

print(next(bee))
print(next(bee))
print(next(bee))