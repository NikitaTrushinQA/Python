#Хороший пароль
#Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру,
#заглавную и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

#Формат входных данных
#На вход программе подаётся одна строка текста.

#Формат выходных данных
#Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.

password = input()
result =all([any(map(lambda x:True if x.isdigit() else False,password)),any(map(lambda x:True if x.isupper() and x.isalpha() else False,password)),any(map(lambda x:True if x.islower() and x.isalpha() else False,password)),len(password)>=7])
if result:
    print('YES')
else:
    print('NO')