# Большое число
# Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
# Все языки	0.055 секунд	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
# Node.js 14.15.5	0.3 секунды	64Mb
# Python 3.7.3	0.1 секунда	64Mb
# Oracle Java 8	0.3 секунды	64Mb
# OpenJDK Java 11	0.3 секунды	64Mb
# Node JS 8.16	0.3 секунды	64Mb
# Вечером ребята решили поиграть в игру «Большое число».
# Даны числа. Нужно определить, какое самое большое число можно из них составить.

# Формат ввода
# В первой строке записано n — количество чисел. Оно не превосходит 100.
# Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.

# Формат вывода
# Нужно вывести самое большое число, которое можно составить из данных чисел.

# Пример 1
# 3
# 15 56 2

# 56215


# Пример 2
# 3
# 1 783 2

# 78321


# Пример 3
# 5
# 2 4 5 2 10

# 542210
import functools

def largestNumber(nums):
    float_calc = sorted(list(enumerate([n / (10 ** len(str(n)) - 1) for n in nums])),
                  key=lambda x: x[1], reverse=True);

    return int(''.join([str(nums[i[0]]) for i in float_calc]));

def test(expected, result):
    if expected != result:
        print('Error! Was expecting: ', expected, ' -  Received: ', result)
    else:
        print('Excellent: ', result)

test(largestNumber([15, 56, 2]), 56215)
test(largestNumber([1, 783, 2]), 78321)
test(largestNumber([2, 4, 5, 2, 10]), 542210)  