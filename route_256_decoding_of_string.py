decoding_dict = {'a':'00','b':'100','c':'101','d':'11'}       #
t = int(input())
for i in range(t):
    line = input()
    decod_stroka = ''                   #результат
    while len(line)>0:
        if decoding_dict['a'] == line[:2]:
            decod_stroka += 'a'
            line = line[2:]
        elif decoding_dict['b'] == line[:3]:
            decod_stroka += 'b'
            line = line[3:]
        elif decoding_dict['c'] == line[:3]:
            decod_stroka += 'c'
            line = line[3:]
        elif decoding_dict['d'] == line[:2]:
            decod_stroka += 'd'
            line = line[2:]
    print(decod_stroka)