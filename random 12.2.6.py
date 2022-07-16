#IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.

#Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.

def generate_ip():
    import random
    spisok = []
    for i in range(256):
        spisok.append(str(i))
    ip = random.sample(spisok,4)
    ip = ('.').join(ip)
    return ip
