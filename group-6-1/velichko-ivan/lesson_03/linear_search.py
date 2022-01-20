# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм линейного поиска

def linear_search(numbers, x):
    for i in range (len(numbers)):
        if numbers[i] == x:
            return i
    return -1

print(linear_search([2, 3, 6, 11, 23, 29, 33, 100], 33))
print(linear_search([2, 3, 6, 11, 23, 29, 33, 100], 44))