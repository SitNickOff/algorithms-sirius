# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def binary_search(numbers, x):
    first = 0
    last = len(numbers) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if numbers[mid] == x:
            index = mid
        else:
            if x < numbers[mid]:
                last = mid - 1
            else:
                first = mid +1
    return index

print(binary_search([2, 3, 6, 11, 23, 29, 33, 100], 33))
print(binary_search([2, 3, 6, 11, 23, 29, 33, 100], 44))