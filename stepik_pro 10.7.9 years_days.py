# Реализуйте генераторную функцию years_days(), которая принимает один аргумент:
#
# year — натуральное число
# Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.
#
# Примечание 1. Возьмем в качестве примера 2022 год. В январе этого года 31 день, в феврале — 28, в марте — 31, и так далее.
# Тогда генератор, полученный при вызове years_days(2022),
# должен порождать сначала все даты с 1 по 31 января, затем с 1 по 28 февраля, и так далее до 31 декабря.
from datetime import date, timedelta
import calendar
def years_days(year):
    start = date(year,1,1)
    if calendar.isleap(year):
        for i in range(1,367):
            yield start
            start += timedelta(days=1)
    else:
        for i in range(1,366):
            yield start
            start += timedelta(days=1)


dates = years_days(2077)

print(*dates)