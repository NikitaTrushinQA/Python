from datetime import datetime, date


def is_available_date(booked_dates, desired_dates):
    '''Функция принимает на вход список строковых дат, недоступных для бронирования:
    booked_dates = ['04.11.2021', '05.11.2021-09.11.2021'],
    а также строку из даты или периода дат, необходимых для бронирования
    desired _dates = '01.11.2021' или '01.11.2021-04.11.2021'
    Функция возвращает True, если даты доступны для бронирования, иначе False
    '''
    booked = []
    for i in booked_dates:
        if "-" in i:
            list2 = i.split("-")
            start = datetime.strptime(list2[0], "%d.%m.%Y")
            end = datetime.strptime(list2[1], "%d.%m.%Y")
            for j in range(start.toordinal(), end.toordinal() + 1):
                booked.append(datetime.fromordinal(j))
        else:
            booked.append(datetime.strptime(i, "%d.%m.%Y"))
    desired = []
    if "-" in desired_dates:
        list2 = desired_dates.split("-")
        start = datetime.strptime(list2[0], "%d.%m.%Y")
        ends = datetime.strptime(list2[1], "%d.%m.%Y")
        for j in range(start.toordinal(), ends.toordinal() + 1):
            desired.append(datetime.fromordinal(j))
    else:
        desired.append(datetime.strptime(desired_dates, "%d.%m.%Y"))
    for dates in desired:
        if dates in booked:
            return False
            break
    return True
