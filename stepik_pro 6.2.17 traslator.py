#Дана строка соответствия латинскому алфавиту: первый символ строки соответствует букве a, второй — b, третий — c, и так далее.
#Каждый символ соответствует как заглавной, так и строчной буквам. Количество символов в строке совпадает с количеством букв в латинском алфавите.

#Напишите программу, которая с помощью данной строки переводит заданный текст.

#Формат входных данных
#На вход программе в первой строке подается строка соответствия латинскому алфавиту, в следующей — текст, требующий перевода.

#Формат выходных данных
#Программа должна с помощью данной строки соответствия латинскому алфавиту перевести введенный текст и вывести полученный результат.

#Примечание 1. Программа должна игнорировать все символы, не являющиеся латинскими буквами.

#Sample Input 1:

#🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩
#I love Python =)
#Sample Output 1:

#🅘 🅛🅞🅥🅔 🅟🅨🅣🅗🅞🅝 =)
#Sample Input 2:

#😀😄😁😆😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨😫😩🥺😢😭😤😠😡
#Dont be so sad!
#Sample Output 2:

#😆😝😛😩 😄😉 😫😝 😫😀😆!

letters = 'abcdefghijklmnopqrstuvwxyz'
dct={}
other_alphabet = input()
phrase = input().lower()
for i in range(len(letters)):
    dct[letters[i]] = other_alphabet[i]
m = phrase.maketrans(dct)

print(phrase.translate(m))