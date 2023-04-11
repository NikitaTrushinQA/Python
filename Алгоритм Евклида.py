def gcd(a, b):
    """Алгоритм Евклида для нахождения наибольшего общего делителя:"""
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


