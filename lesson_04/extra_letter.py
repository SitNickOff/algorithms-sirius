def extra_letter(s, t):
    i = 0
    for i in s:

        if (i in t) == False :
            return i
        else:
            t = t[:t.find(i)] + t[t.find(i) + 1:]
    return t

def test(s, t, result):
    if extra_letter(s, t) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', extra_letter(s, t))
    else:
        print('Отлично: ', result, '==', extra_letter(s, t))

test('abcd', 'abcde', 'e')
test('go', 'ogg', 'g')
test('xtkpx', 'xkctpx', 'c')
test('yoy', 'yoyi', 'i')
