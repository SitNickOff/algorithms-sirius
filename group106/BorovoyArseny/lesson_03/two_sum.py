# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивны алгоритм 
# с применеием сортировки или вспомогательных структур

from math import pi
import unittest

def two_sum_primary(numbers, sum):
    return -1

def two_sum_optimized(numbers, sum):
    return -1                                       

def test(res, aw_res):
    if res == aw_res:
        print("it's ok")
    else:
        print('not ok')

# test(two_sum_primary([1, 2, 3, 5, 9], 10), [1, 9])
# test(two_sum_optimized([1, 2, 3, 5, 9], 8), [3, 5])
