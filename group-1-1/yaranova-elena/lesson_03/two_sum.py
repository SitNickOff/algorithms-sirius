# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивный алгоритм 
# с применеием сортировки или вспомогательных структур

def two_sum(num, s):
    for i in range(s):
        a=s-i
        if a in num and i in num:
            print(a,i)


num=[1,2,3,4]
s=3
print(two_sum(num,s))


def bin_search(num, x):
    low=0
    high=len(num) - 1

    while low<=high:
        middle = (low+high) //2

        if num[middle]==x:
            return x

        elif num[middle]>x:
            high = middle - 1

        elif num[middle]<x:
            low = middle + 1
    return -1

def two_sum_norm(num, sum):
    num=sorted(num)
    result=[]
    print(num)
    for i in num:
        x=sum-i
        if bin_search(num,x) != -1:
            result.append([bin_search(num,x), i])

    return str(result)



num=[1,2,3,6,5]
sum=7
print('optimized', two_sum_norm(num,sum))

# numbers = list(map(int, input().split()))
# sum = int(input())

# print('primary', two_sum_primary(numbers, sum))
# print('optimized', two_sum_primary(numbers, sum))

