# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def linear_search(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1

print(linear_search([1,2,3,4,5,2,1], 3))