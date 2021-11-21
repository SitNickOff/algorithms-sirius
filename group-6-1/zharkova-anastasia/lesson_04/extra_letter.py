# Есть 2 строки s и t, состоящие только из строчных букв. Строка t получена перемешиванием 
# букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.

# Формат ввода
# На вход подаются строки s и t, разделенные переносом строки. Длины строк 
# не превосходят 1000 символов. Строки не бывают пустыми.

# Формат вывода
# Выведите лишнюю букву.

def extra_letter(s,t):      
    vs = []             
    vt = []
    for i in range(len(s)):
        vs.append(s[i])
    for i in range(len(t)):
        vt.append(t[i])
    vs.sort()           
    vt.sort()
    i = 0
    if len(s) > len(t):         
        vt.append(" ")         
        while i < len(s):
            if vs[i] != vt[i]:      
                return vs[i]
            else:
                i+=1
    else:
        vs.append(" ")              
        while i < len(t):
            if vs[i] != vt[i]:
                return vt[i]
            else:
                i+=1
    return "Нет лишней буквы"
        

def test(s, t, result):
    if extra_letter(s, t) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', extra_letter(s, t))
    else:
        print('Отлично: ', result, '==', extra_letter(s, t))

test('abcd', 'abcde', 'e')
test('go', 'ogg', 'g')
test('xtkpx', 'xkctpx', 'c')
test('abcchd', 'bchda','c')