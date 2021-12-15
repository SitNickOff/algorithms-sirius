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

# Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. Напечатайте все комбинации букв,
# которые можно набрать такой последовательностью нажатий.

# Формат ввода
# На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит 10 символов.

# Формат вывода
# Выведите все возможные комбинации букв через пробел.

# 23
# ad ae af bd be bf cd ce cf

# 92
# wa wb wc xa xb xc ya yb yc za zb zc

def letterCombinations(digits):
    if len(digits) == 0:
        return []
    characters = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    result = []
    solve(digits, characters, result)
    return result


def solve(digits, characters, result, current_string="", current_level=0):
    if current_level == len(digits):
        result.append(current_string)
        return
    for i in characters[int(digits[current_level])]:
        solve(digits, characters, result, current_string + i, current_level + 1)


def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')


test(letterCombinations("23"), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
test(letterCombinations("92"), ['wa', 'wb', 'wc', 'xa', 'xb', 'xc', 'ya', 'yb', 'yc', 'za', 'zb', 'zc'])
