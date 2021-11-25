# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def binary_search(numbers, x):
    low = 0
    high = len(numbers) - 1

    while low <= high:

        mid = (low + high) // 2
        guess = numbers[mid]
        

        if guess == x:
            return mid
        if guess > x:
            high = mid - 1
        else:
            low = mid + 1
        
    return None

print(binary_search([3, 6, 7, 9, 10, 13, 16], 16))
print(binary_search([3, 6, 7, 9, 10, 13, 16], 1))
