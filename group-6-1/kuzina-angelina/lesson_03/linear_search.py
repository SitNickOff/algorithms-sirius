# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def linear_search(numbers, x):
    flag = False
    for i in range(len(numbers)):
        if numbers[i] == x:
            flag = True
            return i
    if flag == False:
        return -1