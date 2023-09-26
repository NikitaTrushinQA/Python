






def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as f:
        x = (i for i in f if i != '\n')
        yield from (i.rstrip() if len(i)<=25 else '...' for i in x)



print(*nonempty_lines('file1.txt'))

