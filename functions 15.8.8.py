#Напишите функцию is_num, используя синтаксис анонимных функций,
#которая принимает строковый аргумент и возвращает значение True,
#если переданный аргумент является числом (целым или вещественным) и False в противном случае.

is_num = lambda x: True if x.replace('-', '').replace('.', '').isdigit()  and x.count('.') < 2 and x.count('-') < 2 and '-' not in x[1:]   else False

#print(is_num('10.34ab')) #False
#print(is_num('10.45'))   #True
#print(is_num('-18'))     #True
#print(is_num('-34.67'))  # True
#print(is_num('987'))     #True
#print(is_num('abcd'))    #False
#print(is_num('123.122.12')) #False
#print(is_num('-123.122'))   #True
#print(is_num('--13.2'))   #False
#print(is_num('1-1'))      #False