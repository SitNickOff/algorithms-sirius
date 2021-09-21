def Optimizd(i):          #делаем функцию, для выявления простого числа
    k = 0
    for y in range(2,int(i**1/2)+1): #мы оптимизируем данную функцию тем, что перебираем делители не все, а только до квадратного корня числа
        if i % y == 0:               #т.к. самый большой множитель данного произведения sqrt(y)*sqrt(y), а если дальше перебирать, то мы просто будем повторно проверять делители
            k +=1           #если делитель от 2 до i (не включая) делиться, то флажок "k"= 1
    if k == 0:              #если же не нашелся делитель - флажок не поменялся - то число делиться на "1" и на само число
        return "число", x, "является простым числом"
    else:                   #если нашелся делитель, то это не просто число
        return "-1"
         
        
x = int(input("Введите число для проверки простоты: "))
print(*Optimizd(x))