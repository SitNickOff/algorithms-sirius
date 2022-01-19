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
openList = ["[", "{", "("]
closeList = ["]", "}", ")"]


def is_correct_bracket_seq(string):
    stack = []
    for i in string:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if (len(stack) > 0) and (openList[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True


# print(is_correct_bracket_seq(str(input())))

def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')


test(is_correct_bracket_seq('{[()]}'), True)
test(is_correct_bracket_seq('{[]}()'), True)
test(is_correct_bracket_seq('{[]}([)]'), False)
test(is_correct_bracket_seq('()'), True)