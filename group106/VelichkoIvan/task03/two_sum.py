# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предложить второе решение, которое оптимизрует наивный алгоритм 
# с применеием сортировки или вспомогательных структур

def two_sum_primary(numbers, sum):
    for i in numbers:
        h_list = numbers
        h_list.remove(i)
        x = sum - i
        for ii in h_list:
            if ii == x:
                stroka = str(i) + ' and ' + str(ii)
                return stroka

def two_sum_optimized(numbers, sum):
    return [3, 5]

numbers = list(map(int, input().split()))
sum = int(input())

print('primary', two_sum_primary(numbers, sum))
# print('optimized', two_sum_primary(numbers, sum))

