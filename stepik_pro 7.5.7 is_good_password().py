# Функция is_good_password() 👀
# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:
# string — произвольная строка

# Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.
import string
def is_good_password(string):
    result=[]
    if len(string)>=9:
        pass
    else:
        return False
    if string != string.upper() and string != string.lower():
        pass
    else:
        return False
    if any(map(lambda x:True if  x.isdigit() else False,string)):
        pass
    else:
        return False
    return True

print(is_good_password('sjkdfsjkdfhjksdfhjkSDFSDAFSADFSADfsdajf'))
