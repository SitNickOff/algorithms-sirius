def linear_search(numbers, x):
    for index in range(len(numbers)):
        if numbers[index] == x:
            return index
    return -1
n = int(input())
numbers =[]
for i in range(n):
    numbers.append(int(input()))
x= int(input())

result = linear_search(numbers, x)
print(result)