# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

# num = [1,2,3,4,5,6,7,8,9]


def leaner_search(numbers, x):

    z = len(numbers)
    i = 0

    while z != 1:

        if numbers[i] == x:
            return i
        elif numbers[i] < x:
            z //= 2
            i += z
        elif numbers[i] > x:
            z //= 2
            i -= z
        # else:
        #     return i
        print(z)
        print(i)

    return -1

# print(linear_search(num, 11))

# def leaner_search(num, x):

#     for index in range(len(num)):
#         if num[index] == x:
#             return index

#     return -1


def test(result, awaitin_result):
    if result == awaitin_result:
        print('ok')
    else:
        print('Ошибка', result, '!=', awaitin_result)

test(leaner_search([2,5,8,11,15], 1), -1)
test(leaner_search([2,5,8,11,15], 8), 2)
test(leaner_search([2,5,8,11,15], 15), 4)
test(leaner_search([2,5,8,11,15], 5), 1)