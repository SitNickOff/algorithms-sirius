# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предложить второе решение, которое оптимизрует наивны алгоритм 
# с применеием сортировки или вспомогательных структур


def two_sum_primary(numbers, sum):
    for i in range(len(numbers)):                       
        for j in range(len(numbers)):                   
            if j != i:                                  
                if numbers[i] + numbers[j] == sum:      
                    return [numbers[i], numbers[j]]
    return -1

def two_sum_optimized(numbers, sum):
    for i in range(len(numbers)):
        if (sum - numbers[i]) in numbers:
            return [numbers[i], sum - numbers[i]]                                      
    return -1                                       

def test(result, aw_result):
    if result == aw_result:
        print('Всё работает! ', result, ' = ', aw_result)
    else:
        print('Ошибка! ', result, ' != ', aw_result)

test(two_sum_primary([1, 2, 3, 5, 9], 10), [1, 9])
test(two_sum_optimized([1, 2, 3, 5, 9], 8), [3, 5])

