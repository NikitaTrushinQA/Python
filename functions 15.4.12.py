#Дан список numbers, содержащий кортежи чисел. Напишите программу,
# которая сортирует и выводит список numbers в соответствии с суммой минимального и максимального элемента кортежа.
#Примечание 1. В этой задаче мы считаем, что кортеж (2, 1, 3) меньше кортежа (6, 4, 5),
# так как 1+3 < 4+6. При этом кортеж (1, 2, 9) равен кортежу (4, 5, 6), так как 1+9 = 4+6
numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
def sort_numbers(numbers):
    return  max(numbers)+min(numbers)
print(sorted(numbers,key=sort_numbers))



