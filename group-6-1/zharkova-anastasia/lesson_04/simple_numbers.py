def simple_numbers(n):          
    k = 0
    for y in range(2, n):
        if n % y == 0:
            k +=1           
    if k == 0:              
        return 'Число', x, 'является простым'
    else:                   
        return 'Заданное число не является простым'
         
        
x = int(input('Введите число для проверки:'))
print(simple_numbers(x))