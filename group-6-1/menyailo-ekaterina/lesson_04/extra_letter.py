# Есть 2 строки s и t, состоящие только из строчных букв. Строка t получена перемешиванием 
# букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.

# Формат ввода
# На вход подаются строки s и t, разделенные переносом строки. Длины строк 
# не превосходят 1000 символов. Строки не бывают пустыми.

# Формат вывода
# Выведите лишнюю букву.

def extra_letter(s, t):
    if len(s) > len(t):
        for i in s:
            if s.count(i) != t.count(i):
                return i
    else:
        for i in t:
            if t.count(i) != s.count(i):
                return i


def test(s, t, result):
    if extra_letter(s, t) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', extra_letter(s, t))
    else:
        print('Отлично: ', result, '==', extra_letter(s, t))

test('abcd', 'abcde', 'e')
test('go', 'ogg', 'g')
test('xtkpx', 'xkctpx', 'c')