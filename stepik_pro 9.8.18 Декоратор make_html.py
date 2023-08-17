# Тег — элемент языка разметки, используемый для форматирования текста.
# Например, текст, заключённый между начальным тегом <small> и конечным тегом </small>,
# отображается с меньшим размером, чем основной текст, а текст между тегами <big> и </big> отображается с большим размером.
#
# Реализуйте декоратор make_html(), который принимает один аргумент:
#
# tag — HTML-тег, например, del
# Декоратор должен обрамлять возвращаемое значение декорируемой функции в HTML-тег tag.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
#
# Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции
# , а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.


import functools
def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            result = f'<{tag}>{func(*args,**kwargs)}</{tag}>'
            return result
        return wrapper
    return decorator


# SampleInput1:
#
# @make_html('del')
# def get_text(text):
#     return text
#
#
# print(get_text('Python'))
#
# SampleOutput1:
# < del > Python < / del >
#
# SampleInput2:
# @make_html('i')
# @make_html('del')
# def get_text(text):
#     return text
#
# print(get_text(text='decorators are so cool!'))
#
# SampleOutput2:
#
# < i > <del > decorators are so cool! < / del > < / i >