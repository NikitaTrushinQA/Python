# Функция is_good_password() 🐍
# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать True, если строка string представляет собой хороший пароль, или возбуждать исключение:
#
# LengthError, если его длина меньше 9 символов
# LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Примечание 1. Исключения LengthError, LetterError и DigitError уже определены и доступны.
# Примечание 2. Приоритет возбуждения исключений в случае невыполнения нескольких условий: LengthError, затем LetterError, а уже после DigitError.

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if  not len(string) >= 9:
        raise LengthError

    if not (string != string.upper() and string != string.lower()):
       raise LetterError

    if not any(map(lambda x: True if x.isdigit() else False, string)):
        raise DigitError
    else:
        return True

try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))




