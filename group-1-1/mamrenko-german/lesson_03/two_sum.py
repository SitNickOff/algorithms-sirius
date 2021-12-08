# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивны алгоритм 
# с применеием сортировки или вспомогательных структур

num_arr = [3, 5, 2, -4, 8, 11]
pair_sum = 8

def two_sum_primary(numbers, sum):
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if numbers[i] + numbers[j] == sum and i != j:
                return [numbers[i], numbers[j]]

def two_sum_optimized(numbers, sum):
    hashTable = {}
    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            print("Pair with sum", pair_sum, "is: (", num_arr[i], ",", complement, ")")
        hashTable[num_arr[i]] = num_arr[i]

def test_primary(expected, result):
    if expected != result:
        print("Try again!")
    else:
        print("Seems OK!")

print(two_sum_primary(num_arr, pair_sum))
test_primary(two_sum_primary(num_arr, pair_sum), [3, 5])
print(two_sum_optimized(num_arr, pair_sum))

