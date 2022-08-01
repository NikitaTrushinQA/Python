#Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно)
# и возвращает приветствие в соответствии с образцом.
#Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.
#Примечание 2. Следующий программный код:

#print(greet('Timur'))
#print(greet('Timur', 'Roman'))
#print(greet('Timur', 'Roman', 'Ruslan'))
#должен выводить:
#Hello, Timur!
#Hello, Timur and Roman!
#Hello, Timur and Roman and Ruslan!
#Примечание 3. Функция greet() должна принимать как минимум один обязательный аргумент!
#Примечание 4. Вызывать функцию greet() не нужно, требуется только реализовать.
def greet(name,*args):
    list2=['Hello',name]
    list2=', '.join(list2)
    list1 = args
    if len(list1)==0:
        a=''
    else:
        a = ' and '+ ' and '.join(args)
    print(f'{list2}{a}!')
    print('Hello, Timur and Roman and Ruslan!')
greet('Timur', 'Roman', 'Ruslan')