
#Количество файлов
#Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу,
# которая выводит единственное число — количество файлов в этом архиве.



from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    x=0
    y=0
    for i in info:
        x+=i.file_size
        y+=i.compress_size
    print(f'Объем исходных файлов: {x} байт(а)')
    print(f'Объем сжатых файлов: {y} байт(а)')
