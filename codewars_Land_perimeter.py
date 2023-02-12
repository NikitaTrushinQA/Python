#Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands.
# Each piece of land will be marked with 'X' while the water fields are represented as 'O'.
# Consider each tile being a perfect 1 x 1 piece of land. Some examples for better visualization:

#['XOOXO',
 #'XOOXO',
 #'OOOXO',
# 'XXOXO',
 #'OXOOO']
#should return: "Total land perimeter: 24".

def land_perimeter(arr):
    total_perimeter = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == "X":
                total_perimeter += 4
                if (x != len(arr) - 1) and (arr[x + 1][y] == 'X'):
                    total_perimeter -= 1
                if (x != 0) and (arr[x - 1][y] == 'X'):
                    total_perimeter -= 1
                if (y != len(arr[0]) - 1) and (arr[x][y + 1] == 'X'):
                    total_perimeter -= 1
                if (y != 0) and (arr[x][y - 1] == 'X'):
                    total_perimeter -= 1
    return f"Total land perimeter: {total_perimeter}"


print(land_perimeter(['XOOXO','XOOXO','OOOXO','XXOXO','OXOOO']))