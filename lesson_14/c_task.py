# C. Золотая лихорадка

# Гуляя по одному из островов Алгосского архипелага, Гоша набрёл на пещеру, 
# в которой лежат кучи золотого песка. К счастью, у Гоши есть с собой рюкзак 
# грузоподъёмностью до M килограмм, поэтому он может унести с собой какое-то 
# ограниченное количество золота.

# Всего золотых куч n штук, и все они разные. В куче под номером i содержится mi 
# килограммов золотого песка, а стоимость одного килограмма — ci алгосских франков.

# Помогите Гоше наполнить рюкзак так, чтобы общая стоимость золотого песка в 
# пересчёте на алгосские франки была максимальной.

# Формат ввода
# В первом аргументе задано целое число M — грузоподъёмность рюкзака Гоши (0 ≤ M ≤ 108).

# Во втором аргументе дано количество куч с золотым песком — целое число n (1 ≤ n ≤ 105).

# В элементе массива из n элементов описаны кучи: i-ая куча задаётся двумя целыми 
# числами ci и mi (1 ≤ ci ≤ 107, 1 ≤ mi ≤ 108).

# Формат вывода
# Выведите единственное число —– максимальную сумму (в алгосских франках), 
# которую Гоша сможет вынести из пещеры в своём рюкзаке.

def solution(m, n, arr):
    pass


def test():
    assert solution(10, 3, [[8, 1], [2, 10], [4, 5]]) == 36 
    assert solution(10000, 1, [[4, 20]]) == 80

test()

# m = int(input())
# n = int(input())
# arr = []
# for i in range(n):
#     e = list(map(int, input().split()))
#     arr.append(e)

# print(solution(m, n, arr))
