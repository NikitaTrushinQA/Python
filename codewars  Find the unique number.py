#There is an array with some numbers. All numbers are equal except for one. Try to find it!

#find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
#find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
#It’s guaranteed that array contains at least 3 numbers.


def find_uniq(arr):
    for char in set(arr):
        if arr.count(char) == 1:
            return char
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))