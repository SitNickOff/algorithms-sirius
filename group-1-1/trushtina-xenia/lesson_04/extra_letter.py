# Есть 2 строки s и t, состоящие только из строчных букв. Строка t получена перемешиванием 
# букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.

# Формат ввода
# На вход подаются строки s и t, разделенные переносом строки. Длины строк 
# не превосходят 1000 символов. Строки не бывают пустыми.

# Формат вывода
# Выведите лишнюю букву.

def extra_letter(s, t):    
    list_s = []             
    list_t = []
    for i in range(len(s)):
        list_s.append(s[i])
    for i in range(len(t)):
        list_t.append(t[i])
    list_s.sort()           
    list_t.sort()
    i = 0
    if len(s) > len(t):         
        list_t.append(" ")         
        while i < len(s):
            if list_s[i] != list_t[i]:      
                return list_s[i]
            else:
                i+=1
    else:
        list_s.append(" ")              
        while i < len(t):
            if list_s[i] != list_t[i]:
                return list_t[i]
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