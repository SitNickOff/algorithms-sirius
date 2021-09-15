def linear_search(numbers, x):
    for index in range(len(numbers)):
        if numbers[index] == x:
            return index

    return -1

def binary_search(numbers,x):
    return -1
    


n = 2
numbers = [10,3,25,38,14,1,28,45]
x=28
right_result = 6

result1 = linear_search(numbers, x)
result2 = binary_search(numbers, x)

if right_result == result1:
    print("Число линейное", result1, right_result)
else:
    print("Число бинарное", result2, right_result)
