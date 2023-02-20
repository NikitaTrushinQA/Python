#FAKE NEWS
#Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00.
#Напишите программу, которая принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.

#Формат входных данных
#На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

#Формат выходных данных
#Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:

#До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
#Если в данном случае количество часов равно нулю, то вывести нужно только дни.

#Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:

#До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут
#Если в данном случае количество минут равно нулю, то вывести нужно только часы. Аналогично, если количество часов равно нулю, то вывести нужно только минуты.

#Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст:

#Курс уже вышел!
#Примечание 1. Программа должна подбирать правильную форму для существительных «день» и «минута».

from datetime import date,timedelta,datetime

plural_dict = {0: ("день", "дня", "дней"), 1: ("час", "часа", "часов"), 2: ("минута", "минуты", "минут")}

def choose_plural(amount,plural_dict,key):
    if len(str(amount))!=1:
        if str(amount)[-1] in ['0', '5', '6', '7', '8', '9'] or str(amount)[-1] in ['1', '2', '3', '4'] and str(amount)[
            -2] == '1':
            return plural_dict[key][2]
        elif str(amount)[-1] in ['2', '3', '4']:
            return plural_dict[key][1]
        return plural_dict[key][0]
    else:
        if str(amount)[-1] in ['0', '5', '6', '7', '8', '9']:
            return plural_dict[key][2]
        elif str(amount)[-1] in ['2', '3', '4']:
            return plural_dict[key][1]
        return plural_dict[key][0]


start_course=datetime.strptime('08.11.2022 12:00','%d.%m.%Y %H:%M')
current_date=datetime.strptime(input(),'%d.%m.%Y %H:%M')
result=start_course - current_date
result_days= result.days
result_hours=result.seconds // 3600
result_minutes=(result.seconds // 60) % 60
answer='До выхода курса осталось: '
if current_date >=start_course:
    print('Курс уже вышел!')
else:
    if result_days!=0 and result_hours==0 and result_minutes==0:
        answer += f'{result_days} {choose_plural(result_days, plural_dict, 0)}'
    elif result_days == 0 and result_hours != 0 and result_minutes == 0:
        answer += f'{result_hours} {choose_plural(result_hours, plural_dict, 1)}'
    elif result_days == 0 and result_hours == 0 and result_minutes != 0:
        answer += f'{result_minutes} {choose_plural(result_minutes, plural_dict, 2)}'
    elif result_days!=0 and result_hours!=0:
        for k, num in enumerate([result_days, result_hours]):
            if k ==0:
                answer += f'{num} {choose_plural(num, plural_dict, k)} и '
            else:
                answer += f'{num} {choose_plural(num, plural_dict, k)}'
    else:
        for j, number in enumerate([result_days, result_hours, result_minutes]):
            if number != 0:
                if j!=2:
                    answer += f'{number} {choose_plural(number, plural_dict, j)} и '
                else:
                    answer += f'{number} {choose_plural(number, plural_dict, j)}'
    print(answer)

