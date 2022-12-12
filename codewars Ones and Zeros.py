#Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

#Examples:

#Testing: [0, 0, 0, 1] ==> 1
#Testing: [0, 0, 1, 0] ==> 2
#Testing: [0, 1, 0, 1] ==> 5
#Testing: [1, 0, 0, 1] ==> 9
#Testing: [0, 0, 1, 0] ==> 2
#Testing: [0, 1, 1, 0] ==> 6
#Testing: [1, 1, 1, 1] ==> 15
#Testing: [1, 0, 1, 1] ==> 11
#However, the arrays can have varying lengths, not just limited to 4.


def binary_array_to_number(arr):
    arr = ''.join(list(map(str, arr)))
    result = int(arr, 2)
    return result

print(binary_array_to_number([0, 1, 0, 1]))