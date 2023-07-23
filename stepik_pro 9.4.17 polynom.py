# Функция polynom()
# Реализуйте функцию polynom(), которая принимает один аргумент:
#
# x — вещественное число
# Функция должна возвращать значение выражения x**2 + 1
#
#
# Также функция должна иметь атрибут values, представляющий собой множество (тип set) всех значений функции, которые уже были вычислены.

def polynom(x):
    polynom.__dict__.setdefault('values', set())
    value = x**2 + 1
    polynom.values.add(value)
    return value

print(polynom(5))
print(polynom.values)
