#Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

#For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

#The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
# target will always be the sum of two different items from that array).


#two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]



def two_sum(numbers, target):
    '''функция принимает 2 аргумента: 1) список numbers состоящий из чисел
                                      2) target - число, сумма двух чисел этого списка
        функция должна вернуть список с индексами, тех чисел из numbers ,сумма которых дает target'''
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            #print('i=',i,'j=',j)
            if numbers[i] + numbers[j] == target and i!=j:
                return [i,j]



#print(two_sum([1, 2, 3], 4))   #==> [0,2]
#print(two_sum([1234,5678,9012], 14690))  #==> [1,2]