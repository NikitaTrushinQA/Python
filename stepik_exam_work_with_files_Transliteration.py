#Вам доступен текстовый файл cyrillic.txt, содержащий текст.
#Напишите программу для транслитерации этого файла,
#то есть замены кириллических символов на латинские в соответствии с предложенной таблицей.
#Все остальные символы надо оставить без изменений. Результат транслитерации требуется записать в файл transliteration.txt.
#Формат входных данных
#На вход программе ничего не подается.

#Формат выходных данных
#Программа должна создать файл с именем transliteration.txt в соответствии с условием задачи.

#Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

#Примечание 2. Обратите внимание, что заглавные буквы должны заменяться на соответствующие им заглавные же буквы, но если транслитерационная последовательность состоит из нескольких символов, то заглавным будет только первый из них: «С» на «S», а «Я» на «Ya».

#Примечание 3. Если бы файл cyrillic.txt содержал текст:

#Президент США Дональд Трамп продолжил обмен выпадами с руководством КНДР.
#We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help him: they don’t want the truth to be exposed.
#то содержимое файла transliteration.txt будет:

#Prezident SShA Donal'd Tramp prodolzhil obmen vypadami s rukovodstvom KNDR.
#We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help him: they don’t want the truth to be exposed.

d = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }
with open('cyrillic.txt', encoding = 'utf-8') as file1, open('transliteration.txt', 'a', encoding = 'utf-8') as file2:
    fileList = [file.strip() for file in file1.readlines()]
    for i in fileList:
        stroka = ""
        for j in i:
            if j.lower() in d and j.islower():
                #print("прописная")
                stroka += d[j]
            elif j.lower() in d and j.isupper():
                letter = ""
                if len(d[j.lower()]) > 1:
                    #print("длина больше 1")
                    letter = d[j.lower()][0].upper()+d[j.lower()][1:]
                else:
                    letter = d[j.lower()].upper()
                stroka += letter
            else:
                stroka += j
        file2.write(stroka+'\n')