# Дан массив целых чисел numbers и целое число X;
# нужно найти в массиве два элемента, сумма которых равняется X.
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивны алгоритм
# с применеием сортировки или вспомогательных структур

def two_sum_primary(numbers, sum):
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if numbers[i] + numbers[j] == sum and i != j:
                return [numbers[i], numbers[j]]

def two_sum_optimized(numbersInit, sum):
    numbers = sorted(numbersInit)
    for i in range(len(numbers)):
        if numbers[i] >= sum:
            edge = i
            break
    for i in range(edge):
        for j in range(edge):
            if numbers[i] + numbers[j] == sum and i != j:
                return [numbers[i], numbers[j]]

numbers = [1, 3, 4, 7, 2, 9]
sum = 4
print('primary', two_sum_primary(numbers, sum))
print('optimized', two_sum_primary(numbers, sum))