def Simp(b):
    k = 0
    for i in range(2,int(b**1/2)+1):
        if b % i == 0:
            k+=1
            return True
    if k == 0:
        return False
def factorizate(n):
    array = [ ]
    if Simp(n) == False:         #создаем функцию, которая будет проверять число-простое ли оно. 
        return [n]                   #Если это так, то единственный простой множитель этого число, само число
    elif Simp(n) == True:
        while n > 0:
            print(n)
            print(array)
            if n % 2 == 0:
                array.append(2)
                n //= 2
            elif n % 3 == 0:
                array.append(3)
                n //= 3
            elif n % 5 == 0:
                array.append(5) 
                n //= 5
            if n == 1:
                break
        return array

#n = int(input('введите число, которое надо факторизовать: '))
#print(factorizate(n))

def test(n, result):
    if factorizate(n) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', factorizate(n))
    else:
        print('Отлично: ', result, '==', factorizate(n))

test(8, [2, 2, 2])
test(13, [13])
test(100, [2, 2, 5, 5])