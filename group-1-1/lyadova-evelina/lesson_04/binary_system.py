def change(x):
    n = len(x)-1
    num = ""
    while n > -1:
        t = str(x[n])
        num +=t
        n -=1
    binary = num
    return binary
        
def all(a1, a2):
    y= 0
    binary = ''
    k = 0
    b1 = int(a1)
    b2 = int(a2)
    while b1 > 0 or b2 > 0 or k == 1:
        x = 0
        x1 = b1 % 10
        x2 = b2 % 10
        b1 //=10
        b2 //=10
        x = x1+x2+y
        y = 0
        if x > 1:
            y = 1
            x = 0
        else:
            y = 0
        binary +=str(x)
    if y == 1:
        binary +=str(y)
    return change(binary)

def test(b1, b2, result):
    if all(b1, b2) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', all(b1, b2))
    else:
        print('Отлично: ', result, '==', all(b1, b2))

test('1010', '1011', '10101')
test('1', '1', '10')
test('10110100','10110111', '101001011')