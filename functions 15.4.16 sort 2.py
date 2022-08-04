#Интересная сортировка-2
#На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.

#Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр.
# При этом, если у двух чисел одинаковая сумма цифр, их следует вывести в порядке неубывания.

#Формат входных данных
#На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

#Формат выходных данных
#Программа должна вывести отсортированный список чисел в соответствии с условием задачи, разделяя его элементы одним пробелом.
#111 14 79 7 4 123 90 45 12 171
#12 111 4 14 123 7 45 90 171 79
numbers = input().split()
def sorted_numbers(numbers):
    for k in range(len(numbers)):
        numbers[k]=int(numbers[k])
    numbers = sorted(numbers)
    for h in range(len(numbers)):
        numbers[h] = str(numbers[h])
    a= numbers
    return a

def comparation(item):
    for i in item:
        result = 0
        for j in item:
            result += int(j)
        return result
print(*sorted(sorted_numbers(numbers),key=comparation))



#или
#def numsum(x):
    #return sum(int(n) for n in str(x))

#numbers = [int(i) for i in input().split()]
#print(*sorted(sorted(numbers), key=numsum))