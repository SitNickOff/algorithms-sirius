# Соревнование
#  Все участники турнира разбиваются на пары и соревнуются друг с другом. 
# А потом два самых сильных программиста встречаются в финальной схватке, 
# которая состоит из нескольких раундов. Если в очередном раунде выигрывает 
# первый участник, в таблицу с результатами записывается 0, если второй, то 1. 
# Ничьей в раунде быть не может.

# Нужно определить наибольший по длине непрерывный отрезок раундов, по результатам 
# которого суммарно получается ничья. Например, если 
# дана последовательность 0 0 1 0 1 1 1 0 0 0, то раунды с 2-го по 9-й (нумерация начинается с единицы) дают ничью.

# Формат ввода
# В первой строке задаётся n (0 ≤ n ≤ 10 в 5) –— количество раундов. Во второй 
# строке через пробел записано n чисел –— результаты раундов. Каждое число равно либо 0, либо 1.

# Формат вывода
# Выведите длину найденного отрезка.

def maximum(array):
    pass

def test(result, expected):
    if result == expected:
        print('Ok!')
    else:
        print(f'Ошибка: {result} != {expected}')

test(maximum([0, 1, 0]), 2)
test(maximum([0, 0, 1, 0, 1, 1, 1, 0, 0, 0]), 8)
test(maximum([0, 0, 1, 0, 0, 0, 1, 0, 0, 1]), 4)
test(maximum([1, 0, 0, 0, 1, 0, 0, 1, 0, 0]), 4)
test(maximum([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1]), 2)

test(maximum([1, 1]), 0)
test(maximum([1]), 0)
test(maximum([0, 1]), 2)
test(maximum([]), 0)

data1 = '1 1 1 1 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 1 0 0 1 0 0 1 1 0 0 1 0 0 0 0 1 1 1 0 0 0 1 0 1 1 1 0 1 1 0 0 1 0 0 0 1 0 1 0 0 0 1 1 1 1 1 1 0 1 0 0 0'
data1 = list(map(int, data1.split()))
test(maximum(data1), 46)


data1 = '1 1 0 1 1 1 0 1 0 1 1 1 0 1 0 0 0 0 1 0 0 0 0 1 0 1 0 0 1 1 0 1 1 1 0 1 1 0 0 1 0 0 1 1 1 1 1 0 1 1 0 0 0 0 1 0 0 1 1 1 0 1 1 1 0 1 0 1 1 0 1 0 1 0 1 0 1 1 0 0 0 1 1 1 1 0 0'
data1 = list(map(int, data1.split()))
test(maximum(data1), 70)