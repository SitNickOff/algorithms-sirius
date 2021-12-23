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

def is_correct_bracket_seq(string):
    list_backets = []

    for i in string:
        if i == "[" or i == "]" or i == "(" or i == ")" or i == "{" or i == "}":
            list_backets.append(i)

    if len(list_backets) == 0:
        return True

    elif list_backets.count("[") == list_backets.count("]") and list_backets.count("(") == list_backets.count(
            ")") and list_backets.count("{") == list_backets.count("}"):
        j = 0
        try:
            while j != range(len(list_backets)):
                if list_backets[j] == "(" and list_backets[j + 1] == ")":
                    list_backets.pop(j)
                    list_backets.pop(j)
                    j = 0
                elif list_backets[j] == "{" and list_backets[j + 1] == "}":
                    list_backets.pop(j)
                    list_backets.pop(j)
                    j = 0
                elif list_backets[j] == "[" and list_backets[j + 1] == "]":
                    list_backets.pop(j)
                    list_backets.pop(j)
                    j = 0
                else:
                    j += 1

        except:
            if (len(list_backets)) == 0:
                return True
            else:
                return False

    else:
        return False


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