# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def binary_search(array, num):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + high
        guess = array[mid]

        if guess == num:
            return mid
        if guess > mid:
            high = mid - 1
        if guess < mid:
            low = mid + 1

    return None


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1))
