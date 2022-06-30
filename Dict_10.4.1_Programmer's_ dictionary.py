#Словарь программиста
#Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.

#Формат входных данных
#В первой строке задано одно целое число n — количество слов в словаре.
# В следующих n строках записаны слова и их определения, разделенные двоеточием и символом пробела.
# В следующей строке записано целое число m — количество поисковых слов, чье определение нужно вывести.
# В следующих m строках записаны сами слова, по одному на строке.

#Формат выходных данных
#Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его определение.
# Если слова в словаре нет, программа должна вывести "Не найдено", без кавычек.

#Примечание 1. Мини-словарь для начинающих разработчиков можно посмотреть тут:
# https://ru.hexlet.io/blog/posts/ponimaem-sleng-programmistov-mini-slovar-dlya-nachinayuschih-razrabotchikov.

#Примечание 2. Гарантируется, что в определяемом слове или фразе отсутствует двоеточие (:), следом за которым идёт пробел.

#Sample Input 1:

#5
#Змея: язык программирования Python
#Баг: от англ. bug — жучок, клоп, ошибка в программе
#Конфа: конференция
#Костыль: код, который нужен, чтобы исправить несовершенство ранее написанного кода
#Бета: бета-версия, приложение на стадии публичного тестирования
#3
#Змея
#Жаба
#костыль
#Sample Output 1:
#язык программирования Python
#Не найдено
#код, который нужен, чтобы исправить несовершенство ранее написанного кода

n = int(input())  #вводим n - количество слов в словаре
dict2 = {}
for i in range(n):
    a = input().split(': ')   # отделяем наши будущие ключи и значения в списке
    dict2[a[0].lower()]=a[1] #заполняем словарь ключами и значениями из списка
m = int(input()) # вводим количество поисковых слов, чье определение нужно вывести
for k in range(m):
    word=input()
    result = dict2.get(word.lower(),'Не найдено')
    print(result)

