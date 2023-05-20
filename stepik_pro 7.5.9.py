# Назовем пароль хорошим, если
#
# его длина равна 99 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
#
# Формат входных данных
# На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.
#
# Формат выходных данных
# Для каждого введенного пароля программа должна вывести текст:
#
# LengthError, если длина введенного пароля меньше 99 символов
# LetterError, если в нем все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Success!, если введенный пароль хороший
# После ввода хорошего пароля все последующие пароли должны игнорироваться.
#
# Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий: LengthError, затем LetterError, а уже после DigitError.
#
# Примечание 2. Воспользуйтесь функцией is_good_password() из предыдущей задачи.

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass


def is_good_password(string: str) -> bool:
    if len(string) < 9:
        raise LengthError
    if not (any(map(str.isupper, string)) and any(map(str.islower, string))):
        raise LetterError
    if not any(map(str.isdigit, string)):
        raise DigitError
    return True


import sys
for j in [i.strip() for i in sys.stdin]:
    try:
        is_good_password(j)
        print('Success!')
        break
    except Exception as err:
        print(err.__class__.__name__)
