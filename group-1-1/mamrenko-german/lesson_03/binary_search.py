# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def binarySearch(array, x, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [18, 25, 66, 121, 17, 157, 205]
x = 18

result_ = binarySearch(array, x, 0, len(array)-1)

if result_ != -1:
    print("Index is: " + str(result_))
else:
    print("Not found: -1")