# B. Перевести список ребер в матрицу смежности

# Список рёбер ориентированного графа надо перевести в матрицу смежности. 

# Аргументы функции
# В первом дано число вершин n (1 ≤ n ≤ 100) 
# Во втором - число ребер m (1 ≤ m ≤ n(n-1)). 
# В третьем - список ребер в виде пар вершин (u,v), если ребро ведет от u к v.

# Формат вывода
# Выведите матрицу смежности n на n. На пересечении i-й строки и j-го столбца стоит единица, если есть ребро, ведущее из i в j.

def solution(n, m, edges):
    vs = []
    for i in range(n):
        vs.append([0])
      
    for e in edges:
        # print(f'vs[{e[0]-1}] = {vs[e[0]-1]} ')
        vs[e[0]-1].append(e[1])
        vs[e[0]-1][0] += 1
        
    return vs

def test(result, expected):
    if result != expected:
        print(f'error: {result} != {expected}')

test(
    solution(5, 3, [[1, 3], [2, 3], [5, 2]]), 
    [[1, 3], [1, 3], [0], [0], [1, 2]]
)
test(
    solution(5, 5, [[1, 3], [2, 3], [2, 5], [4, 1], [5, 2]]), 
    [[1, 3], [2, 3, 5], [0], [1, 1], [1, 2]]
)


def solution1(n, m, edges):
    matrix = vs = []
    for i in range(n):
        vs.append([0]*n)
      
    for e in edges:
        matrix[e[0]-1][e[1]-1] = 1
    
    return matrix

def test1(result, expected):
    if result != expected:
        print(f'error: {result} != {expected}')

test1(
    solution1(5, 3, [[1, 3], [2, 3], [5, 2]]), 
    [
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0]
    ]
)