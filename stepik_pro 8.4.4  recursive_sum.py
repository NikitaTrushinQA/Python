# Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:
#
# nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь, также являются либо целые числа,
# либо списки; вложенность может быть произвольной
# Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат.
# Если список nested_lists пуст, функция должна вернуть число 0.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию recursive_sum(), но не код, вызывающий ее.

def recursive_sum(nested_lists):
    summ = 0
    if type(nested_lists) == int:
        summ +=nested_lists
    if type(nested_lists) == list:
        for i in nested_lists:
            summ+=recursive_sum(i)
    return summ


my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))