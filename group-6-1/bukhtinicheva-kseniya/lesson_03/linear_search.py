# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def linear_search(numbers, x):
    for i in range(len(numbers)):
        if numbers[i] == x:
            return i
    return -1

numbers=[1,2,3,4,5,6]
print(numbers)
print(linear_search(numbers,5))
