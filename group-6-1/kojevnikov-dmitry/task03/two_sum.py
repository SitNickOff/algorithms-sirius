# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивны алгоритм 
# с применеием сортировки или вспомогательных структур

num = [1,2,3,4,5,6,7,8,9,10]

def two_sum_primary(numbers, sum):

    for i in range(len(numbers)):

        if numbers[i] + numbers[i + 1] == sum:

            return [numbers[i], numbers[i + 1]]

print(two_sum_primary())


def two_sum_optimized(numbers, sum):
    return [3, 5]

# numbers = list(map(int, input().split()))
# sum = int(input())

# print('primary', two_sum_primary(numbers, sum))
# print('optimized', two_sum_primary(numbers, sum))

