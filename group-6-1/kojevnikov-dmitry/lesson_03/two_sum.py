# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивны алгоритм 
# с применеием сортировки или вспомогательных структур

def two_sum_primary(numbers, sum):
    for i in range(sum):
        a=sum-i
        if a in numbers and i in numbers:
            print(a,i)
            

numbers=[1,2,3,4]
sum=3
print('primary',two_sum_primary(numbers,sum))


def binary_search(numbers, x):
    low=0
    high=len(numbers) - 1

    while low<=high:
        middle = (low+high) //2

        if numbers[middle]==x:
            return x

        elif numbers[middle]>x:
            high = middle - 1

        elif numbers[middle]<x:
            low = middle + 1
    return -1

        


def two_sum_optimized(numbers, sum):
    numbers=sorted(numbers)
    result=[]
    print(numbers)
    for i in numbers:
        x=sum-i
        if binary_search(numbers,x) != -1:
            result.append([binary_search(numbers,x), i])
            
    return str(result)
    
        

numbers=[1,2,3,6,5]
sum=7
print('optimized', two_sum_optimized(numbers,sum))

# numbers = list(map(int, input().split()))
# sum = int(input())

# print('primary', two_sum_primary(numbers, sum))
# print('optimized', two_sum_primary(numbers, sum))

