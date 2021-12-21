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

def worker():
    numD = int(input("Количество детей: "))
    sizeD = sorted(input("Жадность детей: ").split(" "), reverse= True)
    numC = int(input("Количество печенек: "))
    sizeC = sorted(input("Размеры печенек: ").split(" "), reverse= True)
    numHappyD, i, j = 0, 0, 0
    while i < numD and j < numC:
        if sizeC[j] >= sizeD[i]:
            i += 1
            j += 1
            numHappyD += 1
        else:
            i += 1
    print(numHappyD)

worker()