# Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Гарантируется, что возвращаемое значение функции принадлежит типу, который поддерживается форматом JSON.

import json
import functools

def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result =json_data = json.dumps(func(*args,**kwargs))
        return result
    return wrapper


# Sample Input 1:
#
#
# @jsonify
# def make_user(id, live, options):
#     return {'id': id, 'live': live, 'options': options}
#
#
# print(make_user(4, False, None))

# Sample Output 1:
# {"id": 4, "live": false, "options": null}
# Sample Input 2:
#
#
# @jsonify
# def make_list(n):
#     return list(range(1, n + 1))
#
#
# print(make_list(10))
# Sample Output 2:
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Sample Input 3:
#
# @jsonify
# def make_str(s1, s2):
#     return (s1 + s2) * 5
#
#
# print(make_str('bee', 'geek'))
# Sample Output 3:
#
# "beegeekbeegeekbeegeekbeegeekbeegeek"