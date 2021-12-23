# Дерево поиска

# Гоша понял, что такое дерево поиска, и захотел написать функцию, которая определяет, 
# является ли заданное дерево деревом поиска. Значения в левом поддереве должны быть 
# строго меньше, в правом —- строго больше значения в узле.
# Помогите Гоше с реализацией этого алгоритма.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> bool:
    if root is None:
        return "Not found"
    else:
        troot = root
        while troot:
            if root.value < troot.value:
                if troot.left:
                    troot = troot.left
                    if troot.data == root.value:
                        return "Found"
                else:
                    return "Not found"
            elif root.value > troot.value:
                if troot.right:
                    troot = troot.right
                    if troot.data == root.value:
                        return "Found"
                else:
                    return "Not found"
            else:
                return "Found"


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


test()