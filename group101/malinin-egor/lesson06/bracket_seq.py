def is_correct_bracket_seq(string):
    my_stack = []
    open_list = ["[","{","("]
    close_list = ["]","}",")"] 
    if string[0] == ")" or string[0] == "]" or string[0] == "}":
        return False
    for i in string:
        if i in open_list:
            my_stack.append(i)
        elif i in close_list:
            if (open_list[close_list.index(i)] == my_stack[len(my_stack)-1]) and (len(my_stack) > 0):
                my_stack.pop()
            else:
                return False
    if len(my_stack) == 0:
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