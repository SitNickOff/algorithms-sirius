def solution1(n, m, edges):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)

    for e in edges:
        # print(f"edge: {e}")
        matrix[e[0] - 1][e[1] - 1] = 1
    return matrix


def test1(result, expected):
    if result != expected:
        print(f'error: {result} != {expected}')
    else:
        print("Test was successful")


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