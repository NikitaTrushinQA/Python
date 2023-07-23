# Функция remove_marks()
# Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:
#
# text — произвольная строка
# marks — набор символов
# Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.
#
# Также функция remove_marks() должна иметь атрибут count, представляющий собой количество вызовов данной функции.

# Sample Input 1:
# text = 'Hi! Will we go together?'
# print(remove_marks(text, '!?'))
# print(remove_marks.count)

# Sample Output 1:
# Hi Will we go together
# 1

# Sample Input 2:
# marks = '.,!?'
# text = 'Are you listening? Meet my family! There are my parents, my brother and me.'
# for mark in marks:
#     print(remove_marks(text, mark))
# print(remove_marks.count)
#
# Sample Output 2:
#
# Are you listening? Meet my family! There are my parents, my brother and me
# Are you listening? Meet my family! There are my parents my brother and me.
# Are you listening? Meet my family There are my parents, my brother and me.
# Are you listening Meet my family! There are my parents, my brother and me.
# 4

def remove_marks(text,marks):
    remove_marks.__dict__.setdefault('count', 0)
    for i in marks:
        text = text.replace(i,'')
    remove_marks.count+=1
    return text



marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))
print(remove_marks.count)

