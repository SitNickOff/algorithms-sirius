'''from lesson_03.linear_search import linear_search'''
''' def linear_search(numbers, x):
    return -1

def find_element(numbers, x): 
    for index in range(len(numbers)): # проходим по всем элементам массива
        if numbers[index] == x: # сравниваем их с иском
            return index # если нашли - возвращаем индекс
    return -1 # если не нашли - возвращаем индекс

def test(result, awaiting_result):
    if result == awaiting_result:
        print('ok')
    else:
        print('Error', result, 'l=', awaiting_result)

test(linear_search([5, 2, 8, 15, 11], 1), -1)
test(linear_search([5, 2, 8, 15, 11], 8), 2)
test(linear_search([5, 2, 8, 15, 11], 15), 3)
test(linear_search([5, 2, 8, 15, 11], 5), 0)  '''

def find_element(numbers, x):
    
    left = -1
    right = len(numbers)

    while right > left + 1:

        middle = (left + right) // 2

        if numbers[middle] >= x:

            right = middle
        else:

            left = middle

    return right