# Разные деревья поиска

# Ребятам стало интересно, сколько может быть различных деревьев 
# поиска, содержащих в своих узлах все уникальные числа от 1 до n. 
# Помогите им найти ответ на этот вопрос.
# Подсказка: https://www.figma.com/file/qb99LRX3pHJKFQkaXtUvH5/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%3A-%D0%94%D0%B5%D1%80%D0%B5%D0%B2%D1%8C%D1%8F-%D0%B1%D0%B8%D0%BD%D0%B0%D1%80%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0?node-id=0%3A1

# Пример 1
# Ввод: 2
# Вывод: 2


# Пример 2
# Ввод: 3	
# Вывод: 5

# Пример 3
# Ввод 4
# Вывод 14

def trees(n):
    nums = [0] * (n + 1)
    nums[0] = 1
    nums[1] = 1
    for i in range(2, n + 1):
        G(i, nums)
    return nums[n]


def G(i, nums, j=0):
    if j < i:
        nums[i] += nums[j] * nums[i - j - 1]
        G(i, nums, j + 1)


def test(result, expected):
    if result != expected:
        print(f'error: {result} != {expected}')


test(trees(2), 2)
test(trees(5), 42)
test(trees(11), 58786)
