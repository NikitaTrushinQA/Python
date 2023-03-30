#Форматированный вывод
#Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит названия всех файлов из этого архива в лексикографическом порядке,
# указывая для каждого его дату изменения, а также объем до и после сжатия, в следующем формате:

#<название файла>
#  Дата модификации файла: <дата изменения>
#  Объем исходного файла: <объем до сжатия> байт(а)
#  Объем сжатого файла: <объем после сжатия> байт(а)
#Между данными о двух файлах должна располагаться пустая строка.

#Примечание 1. Если файл находится в папке, вывести следует только название без пути.

#Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два пробела):

#Alexandra Savior – Crying All the Time.mp3
#  Дата модификации файла: 2021-11-30 13:27:02
#  Объем исходного файла: 5057559 байт(а)
#  Объем сжатого файла: 5051745 байт(а)

#Hollow Knight Silksong.exe
#  Дата модификации файла: 2013-08-22 08:20:06
#  Объем исходного файла: 805992 байт(а)
#  Объем сжатого файла: 494930 байт(а)

from zipfile import ZipFile
from datetime import datetime
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    d={}
    for i in info:
        d.setdefault(i.filename.split('/')[-1], {}).setdefault('Дата,объем исходного файла,объем сжатого файла', []).append([i.date_time,i.file_size,i.compress_size])
    del d['']
    for key,value in sorted(d.items()):
        print(key)
        print('  Дата модификации файла:',datetime(*value['Дата,объем исходного файла,объем сжатого файла'][0][0]))
        print('  Объем исходного файла:',value['Дата,объем исходного файла,объем сжатого файла'][0][1],'байт(а)')
        print('  Объем сжатого файла:', value['Дата,объем исходного файла,объем сжатого файла'][0][2], 'байт(а)')
        print()

...