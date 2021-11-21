# Любое число раскладывается на произведение простых множителей единственным образом –— с точностью до их перестановки.

# Например, число 8 можно представить как 2 × 2 × 2.

# Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта отличаются лишь порядком следования множителей.

# Разложение числа на простые множители называется факторизацией числа.

# Формат ввода
# В единственной строке дано число n (2 ≤ n ≤ 10 в 9 степени), которое нужно факторизовать.

# Формат вывода
# Выведите в порядке неубывания простые множители, на которые раскладывается число n.

def simple(b):
    k = 0
    for i in range(2,int(b**1/2)+1):
        if b % i == 0:
            k+=1
            return True
    if k == 0:
        return False
        
def factorizate(n):
    array = [ ]
    if simple(n) == False:          
        return [n]                   
    elif simple(n) == True:
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

def test(n, result):
    if factorizate(n) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', factorizate(n))
    else:
        print('Отлично: ', result, '==', factorizate(n))

test(8, [2, 2, 2])
test(13, [13])
test(100, [2, 2, 5, 5])