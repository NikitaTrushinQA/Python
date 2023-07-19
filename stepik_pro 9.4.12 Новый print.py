# Напишите программу, которая переопределяет встроенную функцию print() так,
# чтобы она печатала все переданные строковые аргументы в верхнем регистре.
#
# Примечание 1. Значения sep и end также должны переводиться в верхний регистр.
# Sample Input 1:
# print('beegeek', [1, 2, 3], 4)
# Sample Output 1:
# BEEGEEK [1, 2, 3] 4
#
# Sample Input 2:
# print('bee', 'geek', sep=' and ', end=' wow')
# Sample Output 2:
# BEE AND GEEK WOW
#
# Sample Input 3:
# words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
# print(*words, sep=' to ', end=' LOVE')
# Sample Output 3:
# BLACK TO WHITE TO GREY TO BLACK-1 TO WHITE-1 TO PYTHON LOVE




def new_print(*args,**kwargs):
    result_args = tuple(i.upper() if isinstance(i, str) else i for i in args)
    if kwargs =={}:
        return old_print(*result_args)
    else:
        kwargs['sep'] = kwargs['sep'].upper()
        kwargs['end'] = kwargs['end'].upper()
        return old_print(*result_args,sep=kwargs['sep'], end=kwargs['end'])

old_print = print
print = new_print

words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')