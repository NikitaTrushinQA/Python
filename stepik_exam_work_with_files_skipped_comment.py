name_file = input() # comments.txt
with open(name_file, encoding='utf-8') as file:
    fileList = file.readlines()
    funcs = []
    for i in range(len(fileList)):
        if 'def' in fileList[i] and "#" not in fileList[i-1]:
            funcs.append(fileList[i])
    if len(funcs) == 0:
        print("Best Programming Team")
    else:
        for i in funcs:
            ind1 = i.index(' ')
            ind2 = i.index('(')
            name = i[ind1+1:ind2]
            print(name)