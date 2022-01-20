def binary_search(arr, val):
    arr.sort()
    left = 0 
    right = len(arr)-1
    mid = (left + right)//2

    #Go through the array
    if (val == arr[mid]):
        return mid
    #Check right side of arr
    if (val > arr[mid]):
        return binary_search(arr[mid+1:], val) + (mid + 1)
    #Check left side of arr
    return binary_search(arr[:mid], val)

def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')

test(binary_search([1,2,29,39,923,4432,432],2),1)
test(binary_search([6, 192, 72, 233, 567, 124, 22,1,67], 67), 3)
test(binary_search([6, 192, 72, 233, 567, 124, 22,1,67], 567), 8) 