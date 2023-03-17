#Task
#Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].

#Notes
#Array/list size is at least 2 .
#Array/list's numbers Will be only Positives
#Repetition of numbers in the array/list could occur.
from functools import reduce

def product_array(numbers):
    """Функция принимает список целых чисел(numbers), и возвращает список (prod),
    чтобы prod[i] был равен произведению всех элементов numbers[], кроме numbers[i]."""
    result=[]
    for i in range(len(numbers)):
        result.append(reduce(lambda x,y:x*y,numbers[:i]+numbers[i+1:]))
    return result



#print(product_array([12,20]))     ==>[20,12]
#print(product_array([3,27,4,2]))  ==>[216,24,162,324]
#print(product_array([12,20]))     ==> [900,1170,2340,5850,1300]