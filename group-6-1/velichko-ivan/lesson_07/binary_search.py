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
        print(f'Oh shit Here we go again: {result} != {expected}')
    else:
        print('DAAAAMN U R a GOD')


test(binary_search([12,13,21332,546386,32131,5,2], 12), 0)
test(binary_search([123,123,6575,12334,344,443,1337], 1337),4)
test(binary_search([8,6,4,2,1,3,3,7], 8), 7)