# Комбинации
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв. Примерно так:

# 2:'abc',
# 3:'def',
# 4:'ghi',
# 5:'jkl',
# 6:'mno',
# 7:'pqrs',
# 8:'tuv',
# 9:'wxyz'

# Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. Напечатайте все комбинации букв, которые можно набрать такой последовательностью нажатий.

# Формат ввода
# На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит 10 символов.

# Формат вывода
# Выведите все возможные комбинации букв через пробел.

# 23
# ad ae af bd be bf cd ce cf

# 92
# wa wb wc xa xb xc ya yb yc za zb zc
dict = {
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}

def combination(n, c):
    result = ''
    for i in dict[n]:
        for j in dict[c]:
            result = result + ' ' + i + j 
    return result



def test(result, expected):
    if result != expected:
        print(f'Ошибка!!! {result} != {expected}')
    else:
        print(f'Код работает: {result} == {expected}')

test(combination(2, 3), ' ad ae af bd be bf cd ce cf')