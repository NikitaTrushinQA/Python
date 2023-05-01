# Зоопарк
# Вам доступен файл zoo.json, содержащий список JSON-объектов с данными об обитателях некоторого зоопарка.
# Ключом в каждом объекте является название животного, значением — их количество в зоопарке:
#
# [
#    {
#       "Axolotl": 11,
#       "Poison Frog": 12,
#       "Sonoran Toad": 6,
#       "Tiger Salamander": 16
#    },
#    {
#       "African Fish Eagle": 6,
#       "Andean Condor": 8,
#       "Black Vulture": 8,
#       "Bufflehead Duck": 9,
#       "Flamingo": 8,
#       "Great Horned Owl": 16,
#       "Hornbill": 1
#    },
#    ...
# ]
# Напишите программу, которая определяет, сколько всего животных обитает в зоопарке, и выводит полученный результат.
#
# Примечание 1. Гарантируется, что все ключи в JSON-объектах, различны.



import json
from collections import ChainMap

with open('zoo.json',encoding='UTF-8') as file:
    list_of_animals = json.load(file)
    result = ChainMap(*list_of_animals)
    animals=0
    for value in result.values():
        animals+=value
    print(animals)