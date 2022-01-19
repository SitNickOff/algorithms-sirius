# Скобочная последовательность
# Дана скобочная последовательность. Нужно определить, правильная ли она.
# Будем придерживаться такого определения:
# пустая строка —– правильная скобочная последовательность;
# правильная скобочная последовательность, взятая в скобки одного типа, 
# –— правильная скобочная последовательность;
# правильная скобочная последовательность с приписанной слева или справа 
# правильной скобочной последовательностью —– тоже правильная.
# На вход подаётся последовательность из скобок трёх видов: [], (), {}.
# Напишите функцию is_correct_bracket_seq, которая принимает на вход 
# скобочную последовательность и возвращает True, если последовательность 
# правильная, а иначе False.

# Формат ввода
# На вход подаётся одна строка, содержащая скобочную последовательность. 
# Скобки записаны подряд, без пробелов.

# Формат вывода
# Выведите «True» или «False».

def correct_bracket(string):
    new_string = ''
    dict = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    for i in string:
        if (i == '(') or (i == '{') or (i == '['):
            print(i)
            new_string = new_string + dict[i]
            string = string[:string.find(i)] + string[string.find(i) + 1:] 

    print(string, new_string)


    for i in string:
        if (i in new_string) == True:
            string = string[:string.find(i)] + string[string.find(i) + 1:]
            new_string = new_string[:new_string.find(i)] + new_string[new_string.find(i) + 1:]
    
    if (len(string) > 0) or (len(new_string) > len(string)):
        return False
    else:
        return True

  
def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')

test(correct_bracket('{[()]}'), True)
test(correct_bracket('{[]}()'), True)
test(correct_bracket('{[]}([)]'), False)
test(correct_bracket('()'), True)
test(correct_bracket('{[[}}]]}([)]'), False)
test(correct_bracket('{[{[}]}([)]'), False)


