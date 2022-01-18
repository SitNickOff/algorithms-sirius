# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивны алгоритм 
# с применеием сортировки или вспомогательных структур

def two_sum_primary(numbers, sum):
    for i in numbers:
        for j in numbers:
            if i + j == sum:
                return i, j

def two_sum_optimized(numbers, sum):
    numbers.sort()
    for i in numbers:
        for j in numbers:
            if i + j == sum:
                return i, j

#numbers = list(map(int, input().split()))
#sum = int(input())
print(two_sum_primary([2, 4, 5, 6, 1, 7, 8], 10))
print(two_sum_optimized([2, 4, 5, 6, 1, 7, 8], 10))
# print('primary', two_sum_primary(numbers, sum))
# print('optimized', two_sum_primary(numbers, sum))

