# Любое число раскладывается на произведение простых множителей единственным образом –— с точностью до их перестановки.

# Например, число 8 можно представить как 2 × 2 × 2.

# Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта отличаются лишь порядком следования множителей.

# Разложение числа на простые множители называется факторизацией числа.

# Формат ввода
# В единственной строке дано число n (2 ≤ n ≤ 10 в 9 степени), которое нужно факторизовать.

# Формат вывода
# Выведите в порядке неубывания простые множители, на которые раскладывается число n.

def factorizate(n): #Факторизация числа методом перебора делителей
    loop=2
    flist=[]
    while loop<=n: #Перебор всех целых чисел от 2
        if n%loop==0: #Если остаток от деления равен нулю, то число является делителем
            n//=loop
            flist.append(loop)
        else:
            loop+=1
    return flist


def test(n, result):
    if factorizate(n) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', factorizate(n))
    else:
        print('Отлично: ', result, '==', factorizate(n))

test(8, [2, 2, 2])
test(13, [13])
test(100, [2, 2, 5, 5])