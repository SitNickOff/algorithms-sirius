def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


def is_prime_optimised(num):
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1
    return True


def test(num, result):
    if is_prime(num) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', is_prime(num))
    else:
        print('Отлично: ', result, '==', is_prime(num))


test(7, True)
test(11, True)
test(13, True)
test(100, False)