# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивны алгоритм 
# с применеием сортировки или вспомогательных структур
def sorrt(l,sum_):          #функция созданна для отброски чисел, которые больше суммы
    los = [] 
    for i in range(len(l)):
        if l[i] <= sum_:
            los.append(l[i])
    return los                  

def two_sum_primary(numbers, sum_):
    n = len(numbers)
    for i in range(n):          
        for y in range(n):              
            if numbers[i] + numbers[y] == sum_:
                return [numbers[i], numbers[y]]
    return -1

def two_sum_optimized(numbers, sum_):
    sor = sorrt(numbers,sum_)               
    if (0 in sor) and (sum_ in sor):        
        return [0,sum_]               
    i = n = 0
    k = 1
    while i < len(sor):                      
        if (sor[i] + sor[i+k]) == sum_:        
            return [sor[i],sor[i+k]]
        if k == len(sor)-1-i:
            i +=1
            k = 1
        else:
            k +=1
            continue
    

numbers = list(map(int, input('Введите числа в массив ').split()))
sum_ = int(input('Введите сумму, которую ищем '))
print('primary', two_sum_primary(numbers, sum_))
print('optimized', two_sum_optimized(numbers, sum_))

