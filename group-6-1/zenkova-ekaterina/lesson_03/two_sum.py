# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивны алгоритм 
# с применеием сортировки или вспомогательных структур

def sor(l,sum_):          
    a = [] 
    for i in range(len(l)):
        if l[i] <= sum_:
            a.append(l[i])
    return a                  

def two_sum_primary(numbers, summ):
    n = len(numbers)
    for i in range(n):          
        for y in range(n):              
            if numbers[i] + numbers[y] == summ:
                return [numbers[i], numbers[y]]
    return -1

def two_sum_optimized(numbers, summ):
    s = sor(numbers, summ)               
    if (0 in s) and (summ in s):        
        return [0, summ]               
    i = n = 0
    k = 1 
    while i < len(s):                     
        if (s[i] + s[i + k]) == summ:        
            return [s[i],s[i + k]]
        if k == len(s) - 1 - i:
            i += 1
            k = 1
        else:
            k += 1
            continue
    
numbers = list(map(int, input('Введите числа: ').split()))
summ = int(input('Введите сумму, которую нужно найти: '))

print('Primary', two_sum_primary(numbers, summ))
print('Optimized', two_sum_optimized(numbers, summ))

# numbers = list(map(int, input().split()))
# sum = int(input())

# print('primary', two_sum_primary(numbers, sum))
# print('optimized', two_sum_primary(numbers, sum))
