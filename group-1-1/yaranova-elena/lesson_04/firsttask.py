def simple(n):
    k = 0 
    for i in range(2,int(n**0.5)):
        if n % i ==0:
            return False
    else:
        return True

def test(n, result):
    if simple(n) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', simple(n))
    else:
        print('Отлично: ', result, '==', simple(n))


test(3, True)
test(100, False)
test(5, True)
test(16, False)
test(3, True)