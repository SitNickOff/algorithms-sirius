def binary_Search(arr, x, left = 0, right = None):
    if right == None: 
        right = len(arr)
    if right <= left: 
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == x: 
        return mid
    elif x < arr[mid]:


        return binarySearch(arr, x, left, mid)
    else: 
        return binarySearch(arr, x, mid + 1, right)

arr = [1, 2, 5, 10, 17]
x = 0
index = binary_Search(arr, x)
print(index)