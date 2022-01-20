def binary_search(arr, x, left = 0, right = None):
    if right == None: 
        right = len(arr)
    if right <= left: 
        return -1

    mid = (left + right) // 2
    if arr[mid] == x: 
        return mid
    elif x < arr[mid]: 

        return binary_search(arr, x, left, mid)
    else: 
        return binary_search(arr, x, mid + 1, right)

arr = [1, 2, 6, 12, 21]
x = 6
index = binary_search(arr, x)
print(index) 