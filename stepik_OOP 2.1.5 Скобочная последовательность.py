# Назовем скобочной последовательностью строку, состоящую из символов ( и ). Будем считать скобочную последовательность правильной, если:
#
# для каждой открывающей скобки есть закрывающая скобка
# скобки закрываются в правильном порядке, то есть в каждой паре из открывающей и закрывающей скобок открывающая находится левее
# Напишите программу, которая определяет, является ли скобочная последовательность правильной.
#
# Формат входных данных
# На вход программе подается строка, представляющая собой скобочную последовательность.
#
# Формат выходных данных
# Программа должна вывести True, если введенная скобочная последовательность является правильной, или False в противном случае.

def foo(string):
    x = 0
    if string == '' or len(string) % 2 != 0:
        return False
    else:
        for i in string:
            if i == '(':
                x += 1
                if x < 0:
                    return False
            else:
                x -= 1
                if x < 0:
                    return False
    if x >= 0:
        return True

string = input()
print(foo(string))

# Sample Input 1:
#
# ()()()
# Sample Output 1:
#
# True
# Sample Input 2:
#
# (())
# Sample Output 2:
#
# True
# Sample Input 3:
#
# ()()()(
# Sample Output 3:
#
# False
# Sample Input 4:
#
# )(
# Sample Output 4:
#
# False
# Sample Input 5:
#
# (()))
# Sample Output 5:

# False