# Функции
# DRY - Don't repeat yourself (Не повторяйся)

# Стандартные (встроенные) функции

s1 = 'Python'
print(s1)  # по дргуому функцию не возвращающую значений называют процедурой
length = len(s1)  

count1 = range(10) # Генерирует серию целых чисел от 0 до 9 включительно
count2 = range(1, 10) # Генерирует серию целых чисел от 1 до 9 включительно
count3 = range(1, 10, 2) # Генерирует серию целых чисел от 1 до 9 включительно c шагом 2

print(count1)
print(count2)
print(count3)

print(type(count1))
print(list(count3))

def super_range1(stop):
    answer = []
    i = 0
    while i < stop:
        answer.append(i)
        i += 1

    return answer

s_r1 = super_range1(10)
print('s_r1', s_r1)

def super_range2(stop, start = 0, step = 1):
    answer = []
    i = start
    while i < stop:
        answer.append(i)
        i += step

    return answer

s_r2 = super_range2(10, 1 , 2) # не интуитивно понятный порядок аргументов
print('s_r2', s_r2)


def foo(*args):  # Оператор *args
    print(args)
    # print(args[0])

foo(2, 6, 9) # в результата получим кортеж, значит мы можем обращаться к каждому значению по индексу


def super_range3(*args):
    answer = []

    count = len(args)

    if count == 1:
        start = 0
        stop = args[0]
        step = 1
    elif count == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif count == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        print('Неправильное количество параметров')
        return None

    i = start
    while i < stop:
        answer.append(i)
        i += step

    return answer

print(super_range3(10))
print(super_range3(1, 10))
print(super_range3(1, 10, 2))
print(super_range3(1, 10, 2, 4))

def super_range4(*args, format = 'list'):
    answer = []

    count = len(args)

    if count == 1:
        start = 0
        stop = args[0]
        step = 1
    elif count == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif count == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        print('Неправильное количество параметров')
        return None

    i = start
    while i < stop:
        answer.append(i)
        i += step

    if format == 'list':  # список
        return answer
    if format == 'tuple':  # кортеж
        return tuple(answer)
    if format == 'set':  # сэт
        return set(answer)

    return answer

print(super_range4(1, 10, 2, format = 'list'))
print(super_range4(1, 10, 2, format = 'tuple'))
print(super_range4(1, 10, 2, format = 'set'))

#key word args - словарь. Можем передавать неаграниченное количество неименнованных и именованных параметров
#аргументы могут называться как угодно. Вся соль в звёздочках
def super_range5(*args, **kwargs):  
    answer = []

    count = len(args)

    if count == 1:
        start = 0
        stop = args[0]
        step = 1
    elif count == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif count == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        print('Неправильное количество параметров')
        return None

    i = start
    while i < stop:
        answer.append(i)
        i += step

    if 'format' in kwargs:
        format = kwargs['format']

        if format == 'list':  # список
            return answer
        if format == 'tuple':  # кортеж
            return tuple(answer)
        if format == 'set':  # сэт
            return set(answer)
    else:
        return answer

print(super_range5(1, 10, 2, format = 'list'))
print(super_range5(1, 10, 2, format = 'tuple'))
print(super_range5(1, 10, 2, format = 'set'))