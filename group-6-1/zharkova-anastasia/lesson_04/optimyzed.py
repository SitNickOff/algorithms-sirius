def optimized(n):          
    k = 0
    for y in range(2,int(n**1/2)+1): 
        if n % y == 0:               
            k +=1           
    if k == 0:              
        return print ('Число', x, 'является простым числом')
    else:                   
        return 'Заданное число не является простым'
         
        
x = int(input('Введите число для проверки: '))
print(optimized(x))