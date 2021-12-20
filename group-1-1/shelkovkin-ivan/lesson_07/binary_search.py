def binary_search(arr, val):
    arr.sort()
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    if (val == arr[mid]):
        return mid
    if (val > arr[mid]):
        return binary_search(arr[mid + 1:], val) + (mid + 1)
    return binary_search(arr[:mid], val)


def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')


test(binary_search([1, 3, 15, 23, 122, 652, 12222], 3), 1)
test(binary_search([12, 14, 66, 231, 6555, 785, 122], 122), 3)
test(binary_search([6, 192, 72, 233, 567, 124, 22, 1, 67], 567), 8)