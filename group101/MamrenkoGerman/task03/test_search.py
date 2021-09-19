def linear_search(numbers, x):
    for index in range (len(numbers)):
        if numbers[index] == x:
            return index
    return -1

def binary_search(numbers, x):
    return -1

#n = int(input())
#num = []
#for i in range(n):
#    num.append(int(input()))

#x = int (input())

n = 5
numbers = [10, 3, 25, 38, 14, 1, 28, 45]
x = 38

right_result = 3


result1 = linear_search(numbers, x)
result2 = binary_search(numbers, x)

if right_result == result1:
    print("Порядок!", result1, right_result)
else:
    print("Неверно!", result1, right_result) 

print(result1, right_result)