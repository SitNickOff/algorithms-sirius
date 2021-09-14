numbers = [10, 3, 25, 38, 14, 1, 28, 45]

def binary_search(numbers, x): 
    left = 0 
    right = len(numbers) - 1
    while right > left + 1: 
        middle = (left + right) // 2 
        if numbers[middle] >= x: 
            right = middle 
        else: 
            left = middle 
    return right

result_ = binary_search(numbers, 10)

print(result_)