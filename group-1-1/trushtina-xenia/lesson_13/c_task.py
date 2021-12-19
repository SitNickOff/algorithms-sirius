# C. DFS

# Задан неориентированный граф. Обойдите с помощью DFS все вершины, достижимые 
# из заданной вершины s, и выведите их в порядке обхода, если начинать обход из s.

# Формат ввода
# В первой строке дано количество вершин n (1 ≤ n ≤ 10 в 5) и рёбер m (0 ≤ m ≤ 10 в 5). 
# Далее в m строках описаны рёбра графа. Каждое ребро описывается номерами двух 
# вершин u и v (1 ≤ u, v ≤ n). В последней строке дан номер стартовой вершины s (1 ≤ s ≤ n). 
# В графе нет петель и кратных рёбер.

# Формат вывода
# Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной вершины 
# её соседи будут рассматриваться в порядке возрастания (то есть если вершина 2 соединена 
# с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).

# Пример 1
# Ввод:
# 4 4
# 3 2
# 4 3
# 1 4
# 1 2
# 3
# Вывод:
# 3 2 1 4 

# Пример 2
# Ввод:
# 2 1
# 1 2
# 1

# Вывод:
# 1 2 

n = 4
m = 4
colors = ['white'] * n
# distance = [None] * n
# previous = [None] * n

def solution(n, m, edges):
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

def test(result, expected):
    if result != expected:
        print(f'error: {result} != {expected}')    
        
graph = solution(n, m, [[1, 2], [2, 3], [3, 4], [1, 4]])
test(DFS(solution(4, 4, [[1, 2], [2, 3], [3, 4], [1, 4]]), 3), [3, 2, 4, 1])