# Вам доступен файл planets.txt, содержащий информацию о различных планетах. В первых четырех строках указаны характеристики первой планеты,
# после чего следует пустая строка, затем характеристики второй планеты, и так далее:
#
# Name = Mercury
# Diameter = 4879.4
# Mass = 3.302×10^23
# OrbitalPeriod = 0.241
#
# Name = Venus
# Diameter = 12103.6
# Mass = 4.869×10^24
# OrbitalPeriod = 0.615
#
# ...
# Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.
#
# Функция должна возвращать генератор, порождающий последовательность словарей, каждый из которых содержит информацию об очередной планете из файла planets.txt,
# а именно ее название, диаметр, массу и орбитальный период. Например:
#
# {'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}

def txt_to_dict():
    with open ('planets.txt',encoding='UTF-8') as file:
        data= file.read()
        generator1 = (i.split('\n') for i in data.split("\n\n"))
        for i in generator1:
            d={}
            d = {k.split('=')[0].strip():k.split('=')[-1].strip() for k in i}
            yield d


# Sample Input:
# 
# planets = txt_to_dict()
#
# print(next(planets))
# Sample Output:
#
# {'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}
