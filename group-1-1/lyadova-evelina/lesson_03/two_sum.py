def sorrt(l,sum_): #функция созданна для отброски чисел, которые больше суммы
    los = []
    for i in range(len(l)):
        if l[i] <= sum_:
            los.append(l[i])
    return los #возвращаяем новый список

def two_sum_primary(numbers, sum_):
    n = len(numbers)
    for i in range(n):
        for y in range(n): #перебираем числе несколько раз, тем самым ищем числа, которые дают список
            if numbers[i] + numbers[y] == sum_:
                return [numbers[i], numbers[y]]
    return -1

def two_sum_optimized(numbers, sum_):
    sor = sorrt(numbers,sum_) #осортруем список и удалим нунжные нам элементы(которые больше sum_)
    if (0 in sor) and (sum_ in sor): #заранее можно найти два элемента, которые дают sum_
        return [0,sum_]
    i = n = 0
    k = 1
    while i < len(sor): #в отличии от 1-ого случая(перебирая все элементы),
        if (sor[i] + sor[i+k]) == sum_: #мы будем перебирать только один раз, ища 2-ое слагаемое
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

