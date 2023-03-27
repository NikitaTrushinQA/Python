

#Количество файлов
#Вам доступен архив workbook.zip, содержащий различные папки и файлы.
#Напишите программу, которая выводит единственное число — количество файлов в этом архиве.

#Примечание 1. Обратите внимание, что папка не считается файлом.


from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    result = 0
    for i in info:
        if i.is_dir()==False:
            result+=1
print(result)
