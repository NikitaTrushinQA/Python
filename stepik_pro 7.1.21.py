# Требовалось реализовать функцию swapcase_vowels(), которая принимает в качестве аргумента строку,
# заменяет в ней все гласные латинские буквы на заглавные и возвращает полученную новую строку.
# Программист торопился и реализовал функцию неправильно.

def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char in vowels:
            swapped_string += char.upper()
        else:
            swapped_string +=char
    return swapped_string