#Реализуйте функцию print_given(), которая принимает произвольное количество позиционных
# и именованных аргументов и выводит все переданные аргументы, указывая тип каждого.
# Пары аргумент-тип должны выводиться каждая на отдельной строке, в следующем формате:

#для позиционных аргументов:
#<значение аргумента> <тип аргумента>
#для именованных аргументов:
#<имя переменной> <значение аргумента> <тип аргумента>
#Примечание 1. При выводе позиционные аргументы должны быть расположены в порядке их передачи,
# именованные — в лексикографическом порядке имен переменных.

#Примечание 2. При выводе сначала должны следовать все позиционные аргументы, затем — все именованные.

#Примечание 3. Если в функцию ничего не передается, функция ничего не должна выводить.

def print_given(*args,**kwargs):
    for i in args:
        print(i,type(i))
    for j in sorted(kwargs.keys()):
        print(j, kwargs[j], type(kwargs[j]))






