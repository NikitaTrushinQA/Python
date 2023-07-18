# Функция verification()
# Реализуйте функцию verification(), которая проверяет правильность введенного пароля. Она должна принимать четыре аргумента в следующем порядке:
#
# login — логин пользователя
# password — пароль пользователя
# success — некоторая функция
# failure — некоторая функция

# Пароль считается правильным, если в нем присутствует,
# хотя бы одна заглавная латинская буква,
# хотя бы одна строчная латинская буква и хотя бы одна цифра.

# Функция verification() должна вызывать функцию success() с аргументом login,
# если переданный пароль является правильным,
# иначе — функцию failure() с аргументами login и строкой-сообщением об ошибке:
#
# в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
# в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
# в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
# в пароле нет ни одной цифры, если в пароле отсутствуют цифры
# Примечание 1. Если пароль не удовлетворяет нескольким условиям, то приоритеты выбора строки-сообщения об ошибке являются следующими:
#
# в пароле нет ни одной буквы
# в пароле нет ни одной заглавной буквы
# в пароле нет ни одной строчной буквы
# в пароле нет ни одной цифры
import string

low_letters = string.ascii_lowercase
up_letters = string.ascii_uppercase
letters = string.ascii_letters
d = { 0: 'в пароле нет ни одной буквы',
      1: 'в пароле нет ни одной заглавной буквы',
      2: 'в пароле нет ни одной строчной буквы',
      3: 'в пароле нет ни одной цифры'}

def verification(login,password,success,failure):
    result = [any(map(lambda x: True if x in letters else False, password)),
              any(map(lambda x: True if x in up_letters else False, password)),
              any(map(lambda x: True if x in low_letters else False, password)),
              any(map(lambda x: True if x.isdigit()  else False, password)),
             ]
    if all(result):
        return success(login)
    return failure(login,d.get(result.index(False)))



def success(login):
    print(f'Здравствуйте, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)
#Arthur_Davletov, попробуйте снова. Текст ошибки: в пароле нет ни одной строчной буквы
