# Реализуйте функцию get_digits() c использованием аннотаций типов, которая принимает один аргумент:
#
# number — положительное целое или вещественное число
# Функция должна возвращать список, состоящий из цифр числа number.
#
# Примечание 1. Используйте встроенные типы (list, tuple, ...),
# а не типы из модуля typing. Также используйте нотацию |, а не тип Union из модуля typing.
#
# Примечание 2. Порядок следования цифр в списке должен совпадать с порядком следования их в исходном числе.

def get_digits(number: int | float)->list[int]:
    return [int(i)  for i in str(number) if i.isdigit()]

annotations = get_digits.__annotations__

print(annotations['number'])
#int | float