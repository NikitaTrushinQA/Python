# Итератор Fibonacci
# Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.
#
# Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 1.
#
# Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой двух предыдущих:
# 1, 1, 2, 3, 5, 8, 13, 21, 34

class Fibonacci:
    def __init__(self):
        self.first = 1
        self.second = 0

    def __iter_(self):
        return self

    def __next__(self):
        value = self.first + self.second
        self.first, self.second = self.second, value
        return value

#1
#

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

