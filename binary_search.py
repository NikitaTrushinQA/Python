def binary_search(data, elem):
    """бинарный поиск
        Этот алгоритм используется для поиска элемента в упорядоченной последовательности (например: список, кортеж или строка).
"""
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) // 2
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1

#print(binary_search([1,2,55,66,111,222,333,666],55))



