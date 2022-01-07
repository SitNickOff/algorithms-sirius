# Формат ввода
# Два числа в двоичной системе счисления, каждое на отдельной строке.
# Длина каждого числа не превосходит 10 000 символов.

# Формат вывода
# Одно число в двоичной системе счисления.

# Пример 1

# Ввод:
# 1010
# 1011

# Вывод:
# 10101

# Пример 2

# Ввод:
# 1
# 1

# Вывод:
# 10

def less4BynarySystem():
    a = input("a: ")
    b = input("b: ")
    n = len(a)- len(b)
    if n >= 0:
        for i in range(n):
            b = "0" + b
    else:
        for i in range (0, n, -1):
            a = "0" + a
    result = ""
    l = 0
    for i in range(len(a)-1, -1, -1):
        k = (int(a[i])) + (int(b[i])) + l
        if k == 0:
            result = "0"+ result
            l = 0
        if k == 1:
            result = "1"+ result
            l = 0
        if k == 2:
            result = "0"+ result
            l = 1
        if k == 3:
            result = "1"+ result
            l = 1
        if i  == 0:
            result = str(l) + result
    print(result)

less4BynarySystem()