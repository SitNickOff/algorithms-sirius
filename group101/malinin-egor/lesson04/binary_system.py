def add(b1, b2):
    b22 = b2[::-1]
    binary = ''
    j = 0
    sum = 0
    for i, value in enumerate(b1[::-1], 0):
        sum = int(value) + int(b22[i]) + j
        if sum < 2:
            binary = str(sum) + binary
            j = 0
        elif j > 0:
            binary = '1' + binary
            j -=1
        elif j == 0:
            binary = '0' + binary
            j +=1
    while j != 0:
         binary = '1' + binary
         j -= 1

    return binary

def test(b1, b2, result):
    if add(b1, b2) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', add(b1, b2))
    else:
        print('Отлично: ', result, '==', add(b1, b2))

test('1010', '1011', '10101')
test('1', '1', '10')
test('1', '2', '11')