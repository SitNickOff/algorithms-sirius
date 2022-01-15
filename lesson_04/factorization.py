def factorizate(n):
    i = 2
    num = []
    while (n != 1) or (n == i):
        if n % i == 0:
            n = n / i
            num.append(i)
            i = 2
            print(num)
        else:
            i += 1
    return num

def test(n, result):
    if factorizate(n) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', factorizate(n))
    else:
        print('Отлично: ', result, '==', factorizate(n))

test(8, [2, 2, 2])
test(13, [13])
test(100, [2, 2, 5, 5])
test(14, [7, 2])
