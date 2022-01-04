# A. Построить список смежности

# Для очень большого числа ориентированных графов необходимо преобразовать их список рёбер 
# в список смежности. Необходимо написать программу, которая по списку рёбер графа будет строить его список смежности.

# Аргументы функции
# В первом дано число вершин n (1 ≤ n ≤ 100) 
# Во втором - число ребер m (1 ≤ m ≤ n(n-1)). 
# В третьем - список ребер в виде пар вершин (u,v), если ребро ведет от u к v.

# Формат вывода
# Выведите информацию о рёбрах, исходящих из каждой вершины.

# В строке i надо написать число рёбер, исходящих из вершины i, а затем перечислить вершины, 
# в которые ведут эти рёбра –— в порядке возрастания их номеров.

def solution(n, m, edges):
    vs = []
    for i in range(n):
        vs.append([0])
    
    for e in edges:
        vs[e[0]-1][0] += 1
        vs[e[0]-1].append(e[1])
    
        # print(f'e: {e}')
        # print(f'vs[e[0]-1]: {vs[e[0]-1]}')
    
    # print(f'vs: {vs}')
    return vs

def test(result, expected):
    if result != expected:
        print(f'error: {result} != {expected}')
    else:
        print("OK")

test(
    solution(5, 3, [[1, 3], [2, 3], [5, 2]]), 
    [[1, 3], [1, 3], [0], [0], [1, 2]]
)
test(
    solution(5, 5, [[1, 3], [1, 5], [2, 3], [3, 5], [5, 2]]), 
    [[2, 3, 5], [1, 3], [1, 5], [0], [1, 2]]
)


def solution1(n, m, edges):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    
    for e in edges:
        # print(f"edge: {e}")
        matrix[e[0]-1][e[1]-1] = 1
    return matrix

def test1(result, expected):
    if result != expected:
        print(f'error: {result} != {expected}')
    else:
        print("Ok")

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

test1(
    solution1(5, 5, [[1, 3], [1, 5], [2, 3], [3, 5], [5, 2]]), 
    [
        [0, 0, 1, 0, 1], 
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0]
    ]
)



n = 4
m = 4
colors = ['white'] * n
# distance = [None] * n
# previous = [None] * n

graph = solution(n, m, [[1, 2], [2, 3], [3, 4], [1, 4]])


    

# def BFS(s):
#     planned = []
#     planned.append(s)
    
#     print(f'planned: {planned}')

# print(graph)
# BFS(1)

def solution2(n, m, edges):
    vs = []
    for i in range(n):
        vs.append([])
    
    for e in edges:
        vs[e[0]-1].append(e[1])
        vs[e[1]-1].append(e[0])
    
    return vs

def DFS(graph, s, order = [], visited = []):
    visited = [False] * len(graph)
    order.append(s)
    print(f'graph[s-1]: {graph[s-1]}')
    visited[s-1] = True
    
    for e in graph[s-1]:
        print(e)
        if not visited[e-1]:
            DFS(graph, e, order, visited)
        
    print(f'graph: {graph}')    
    print(f'visited: {visited}')

    return order
    
test(DFS(solution2(4, 4, [[1, 2], [2, 3], [3, 4], [1, 4]]), 3), [3, 2, 4, 1])
