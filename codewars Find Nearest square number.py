#Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.

#For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121, since 111 is closer to 121, the square of 11,
# than 100, the square of 10.

#If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

def nearest_sq(n):
    if n**(1/2)==int(n**(1/2)):
        return n
    else:
        return int(n**(1/2))**2 if abs(n-int(n**(1/2))**2) < abs(n-int(n**(1/2)+1)**2) else (int(n**(1/2))+1)**2



