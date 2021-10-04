from math import pi
import unittest

def two_sum_primary(numbers, sum):
    for i in range(len(numbers)):                       
        for j in range(len(numbers)):                   
            if j != i:                                  
                if numbers[i] + numbers[j] == sum:      
                    return [numbers[i], numbers[j]]
    return -1

def two_sum_optimized(numbers, sum):
    for i in range(len(numbers)):
        if (sum - numbers[i]) in numbers:
            return [numbers[i], sum - numbers[i]]                                      
    return -1                                       

def test(res, aw_res):
    if res == aw_res:
        print("it's ok")
    else:
        print('not ok')

test(two_sum_primary([1, 2, 3, 5, 9], 10), [1, 9])
test(two_sum_optimized([1, 2, 3, 5, 9], 8), [3, 5])