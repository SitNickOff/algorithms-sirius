# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивны алгоритм 
# с применеием сортировки или вспомогательных структур
def two_sum(array, num):
    for i in array:
        if (num - i) in array:
            return [i, num - i]
    return None

def test_two_sum(result, expected):
    if result != expected:
        print(f'error')
    else:
        print(f'Ok: {result} = {expected}')

test_two_sum(two_sum([1,2,3,5,7,9], 9), [2, 7])


