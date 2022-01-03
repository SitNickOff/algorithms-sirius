def extra(s,t):      
    vs = []             #переносим элементы строки в массив
    vt = []
    for i in range(len(s)):
        vs.append(s[i])
    for i in range(len(t)):
        vt.append(t[i])
    vs.sort()           #отсортируем, тем самым программа позже найдет не соответсвия в соортировке 2-ух массивов
    vt.sort()
    i = 0
    if len(s) > len(t):         #если 2 строка меньше 1
        vt.append(" ")         #задаем пустое значение, т.к. другой массив будет больше и при алгоритме выдаст ошибку "выход за пределы массива"
        while i < len(s):
            if vs[i] != vt[i]:      #в отсортированном массиве проверям, все ли буквы на месте
                return vs[i]
            else:
                i+=1
    else:
        vs.append(" ")              #тоже самое выполняем, если 1 строка меньше 2
        while i < len(t):
            if vs[i] != vt[i]:
                return vt[i]
            else:
                i+=1
    return "нет лишней буквы"
        

def test(s, t, result):
    if extra(s, t) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', extra(s, t))
    else:
        print('Отлично: ', result, '==', extra(s, t))

test('abcd', 'abcde', 'e')
test('go', 'ogg', 'g')
test('xtkpx', 'xkctpx', 'c')
test('abcchd', 'bchda','c')