def is_prime(number):
    if number == 1:
        return False
    g = 0
    for i in range(2, number):
        if number % i == 0:
            g +=1
    if g == 0:
        return True
    return False
def test(number, result):
    if is_prime(number) != result:
        print('Ошибка! Ожидаем: ', result, ' - Получаем: ', is_prime(number))
    else :
        print('Всё отлично!')

test(1, False)
test(7, True)
test(4, False)
test(13, True)