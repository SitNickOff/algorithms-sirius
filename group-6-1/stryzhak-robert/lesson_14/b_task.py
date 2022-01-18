# B. Расписание
# 
# Дано количество учебных занятий, проходящих в одной аудитории. Для каждого из 
# них указано время начала и конца. Нужно составить расписание, в соответствии 
# с которым в классе можно будет провести как можно больше занятий.

# Если возможно несколько оптимальных вариантов, то выведите любой. 
# Возможно одновременное проведение более чем одного занятия нулевой длительности.

# Формат ввода
# В первой аргументе задано число занятий. Оно не превосходит 1000. 
# Во втором аргументе задан массив занятий, каждый элемент которого состоит массива 
# двух элементов: [время_начала, время_окончания]. 
# Время задаётся одним целым числом h, если урок начинается/заканчивается ровно в h часов. 
# Если же урок начинается/заканчивается в h часов m минут, то время записывается как h.m. 
# Гарантируется, что каждое занятие начинается не позже, чем заканчивается. Указываются только значащие цифры.

# Формат вывода
# Выведите в первой строке наибольшее число уроков, которое можно провести в аудитории. 
# Далее выведите время начала и конца каждого урока в отдельной строке в порядке их проведения.

def scheduler(arr):
    all_1 = len(arr)
    res = 0 
    res_arr = [0,0]
    result = []
    for i in range(all_1):
        lesson = arr[i]
        if lesson[0] == lesson[1]:
            res += 1
        if lesson[0] > res_arr[1] or lesson[1] < res_arr[0]:
            res_arr = lesson
            result.append(res_arr)
            res += 1
    return (res,result)

        
def test(result,expected):
    if result != expected:
        print (f'error: {result} != {expected}')
def test_!():
    test(scheduler([
        [9, 10], [9.3, 10.3], [10, 11], [10.3, 11.3], [11, 12]
    ]) == (3, [[9, 10], [10, 11], [11, 12]]))

    assert scheduler([
        [9, 10], [11, 12.25], [12.15, 13.30]
    ]) == (2, [[9, 10], [11, 12.25]])

    assert scheduler([
        [19, 19], [7, 14], [12, 14], [8, 22], [22, 23], [5, 21], [9, 23]
    ]) == (3, [[7, 14], [19, 19], [22, 23]])

    assert scheduler([
        [15, 22], [17, 20], [12, 13], [21, 23], [15, 15], 
        [3, 23], [20, 23], [7, 18], [11, 13], [2, 16],
        [7, 19], [1, 10], [16, 23], [15, 17], [15, 19],
        [12, 14], [8, 9], [8, 17], [19, 23], [12, 15], 
        [3, 10], [3, 8], [17, 20], [20, 21], [0, 0],
        [17, 21], [13, 17], [2, 23], [20, 20], [18, 19],
        [9, 10], [7, 10], [23, 23], [22, 22], [8, 10],
        [4, 9], [21, 21], [18, 22], [14, 19], [19, 20],
        [22, 23], [12, 22], [3, 9], [15, 23], [2, 21],
        [8, 8], [10, 15], [13, 13], [0, 7], [11, 19],
        [0, 22], [2, 6], [15, 16], [5, 8], [20, 23],
        [18, 23], [11, 22], [17, 20], [12, 14]
    ]) == (17, [
        [0, 0], [2, 6], [8, 8], [8, 9], [9, 10],
        [11, 13], [13, 13], [15, 15], [15, 16], [18, 19],
        [19, 20], [20, 20], [20, 21], [21, 21], [22, 22],
        [22, 23], [23, 23]
    ])

test()

#