# Печеньки
# Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
# Все языки	0.05 секунд	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
# Node.js 14.15.5	0.15 секунд	64Mb
# Python 3.7.3	0.08 секунд	64Mb
# Oracle Java 8	0.4 секунды	64Mb
# OpenJDK Java 11	0.4 секунды	64Mb
# Node JS 8.16	0.15 секунд	64Mb
# К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.

# Но не всё так просто. Печенья могут быть разного размера. А у каждого ребёнка есть фактор жадности —– минимальный размер печенья, которое он возьмёт. Нужно выяснить, сколько ребят останутся довольными в лучшем случае, когда они действуют оптимально.

# Каждый ребёнок может взять не больше одного печенья.

# Формат ввода
# В первой строке записано n —– количество детей.

# Во второй —– n чисел, разделённых пробелом, каждое из которых –— фактор жадности ребёнка. Это натуральные числа, не превосходящие 1000.

# В следующей строке записано число m –— количество печенек.

# Далее —– m натуральных чисел, разделённых пробелом —– размеры печенек. Размеры печенек не превосходят 1000.

# Оба числа n и m не превосходят 10000.

# Формат вывода
# Нужно вывести одно число –— количество детей, которые останутся довольными

# Пример 1
# 2
# 1 2
# 3
# 2 1 3

# 2


# Пример 2
# 3
# 2 1 3
# 2
# 1 1

# 1

def insertion_sort(array):
    for i in range(len(array)):
        item_to_insert = array[i]
        j = i

        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1

        array[j] = item_to_insert
    return array


def hungry_child(a, b):
    statis =list(map(int, b.split()))
    children = len(statis)
    coockies = list(map(int, a.split()))
    quant_cild = len(coockies)
    pleased = 0

    

    insertion_sort(statis)
    insertion_sort(coockies)

    for i in range(len(statis)) :
        item_to_insert = statis[i]
        j = i

        

        while j < children and j < quant_cild :
            print('i',i)
            print('j',j)
            print('cildren', children, 'quant', quant_cild)
            print(statis, coockies)
            if coockies[i] >= statis[j]:
                pleased += 1
                # coockies.pop(i)
                # statis.pop(j)
                break
            elif j < len(b):
                j +=1
            else:
                break
    return pleased


def test(result, expected):
    if result != expected:
        print(f'Ищи косяк... {result} != {expected}')
    else:
        print('Чудо свершилось - код работает')

test(hungry_child('1 2', '3 1 2'), 2)
test(hungry_child('2 1 3', '1 1'), 1)
test(hungry_child('9 5 3', '10 2 7 12'), 3)



        




