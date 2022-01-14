# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def binary_search(numbers, x):
    
    left = -1
    right = len(numbers)
    if x in numbers:
        while right > left +1:
            middle = (left + right) // 2
            if numbers[middle] >= x:
                right = middle 
            else:
                left = middle 
        return right
    else:
        return -1
    

def test(result,awaiting_res):
    if result == awaiting_res:
        print("ok")
    else:
        print('not ok')


a = [10,2,3,6,8,1]
print('введите символ для поиска в списке')
n = int(input())
print(sorted(a))
print(binary_search(sorted(a),n))
a.sort()
test(binary_search(a, 1), 0)
test(binary_search(a, 2), 1)
test(binary_search(a, 15), -1)
test(binary_search(a, 5), -1)