#Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 2 десятичных знаков,
#а затем выводит их, каждый на отдельной строке.
def rounded(x):
    return round(x,2)

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

print(*map(rounded, numbers), sep = '\n')
