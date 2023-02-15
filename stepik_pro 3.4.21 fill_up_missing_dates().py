#Функция fill_up_missing_dates()
#Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:

#dates — список строковых дат в формате DD.MM.YYYY
#Функция должна возвращать список, в котором содержатся все даты из списка dates,
# расположенные в порядке возрастания, а также все недостающие промежуточные даты.

#Примечание 1. Рассмотрим первый тест. Список dates содержит период с 01.11.2021 по 07.11.2021:

#dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
#в котором отсутствуют даты 02.11.2021, 05.11.2021, 06.11.2021. Тогда вызов функции:
#fill_up_missing_dates(dates)
#должен вернуть список:

#['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']
#Примечание 2. Функция должна создавать и возвращать новый список, а не изменять переданный.

from datetime import date,datetime,timedelta

def fill_up_missing_dates(dates):
    result = []
    new_list_of_dates = []
    for i in dates:
        d, m, y = map(int, i.split('.'))
        date2 = date(y, m, d).toordinal()
        new_list_of_dates.append(date2)
    print(new_list_of_dates)
    #maximum= datetime.strptime(max(dates), '%d.%m.%Y')
    #minimum=datetime.strptime(min(dates), '%d.%m.%Y')
    maximum=max(new_list_of_dates)
    maximum = date.fromordinal(maximum)
    minimum=min(new_list_of_dates)
    minimum=date.fromordinal(minimum)
    for j in range(minimum.toordinal(), (maximum+timedelta(days=1)).toordinal()):
        a = date.fromordinal(j)
        result.append(a.strftime('%d.%m.%Y'))
    return result


#print(fill_up_missing_dates(['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']))
#print(len(fill_up_missing_dates(['20.07.2021', '16.05.2021', '19.01.2021', '18.11.2021', '17.10.2021', '15.03.2021']))) ==>#304

