# Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:
#
# language — код языка: ru — русский, en — английский
# Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:
#
# русского алфавита, если language имеет значение ru
# английского алфавита, если language имеет значение en
# Примечание 1. Буква ё в русском алфавите не учитывается.
import string
class Alphabet:
    def __init__(self,language):
        dct = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}
        self.language = language
        self.letters = dct.get(self.language)

    def __iter__(self):
        return self

    def __next__(self):
        pass