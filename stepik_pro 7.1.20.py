# Дан файл data.txt. Требовалось написать программу, которая определяет, сколько строк содержится в данном файле, и выводит полученный результат.
# Программист торопился и написал программу неправильно.


total = 0

with open('data.txt', encoding='utf-8') as file:
    for _ in file.readlines():
        total = total + 1

print(total)