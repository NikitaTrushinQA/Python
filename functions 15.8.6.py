#Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True,
#если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен) и False в противном случае.

func = lambda x: True if x[0] in 'aA' and x[-1] in 'aA' else False