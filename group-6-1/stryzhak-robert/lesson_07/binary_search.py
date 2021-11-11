def binary_search_iterative(arr, elem):
    start, end = 0, (len(arr) - 1)
    while start <= end:
        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        if elem < arr[mid]:
            end = mid - 1
        else:  # elem > arr[mid]
            start = mid + 1

    return False

a = [1,1,2,3,4,5,6,67,543,23,23,21,12,122]
print(binary_search_iterative(a,122))