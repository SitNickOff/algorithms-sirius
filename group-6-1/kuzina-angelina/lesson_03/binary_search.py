# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def binary_search(numbers, x):
    numbers.sort()
    left = -1 
    right = len(numbers)
    while right > left + 1:
        middle = (left + right) // 2
        if numbers[middle] >= x:
            right = middle
        else:
            left = middle
    if right == x:
        return right
    else:
        return -1