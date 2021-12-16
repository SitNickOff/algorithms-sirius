# Напишите функцию solution, 
# которая принимает на вход голову списка и номер удаляемого дела и 
# возвращает голову обновлённого списка.

# Внимание: в этой задаче не нужно считывать входные данные. Нужно написать 
# только функцию, которая принимает на вход голову списка и номер удаляемого 
# элемента и возвращает голову обновлённого списка.

class Node:  
    def init(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node

def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next_item
    print("None")

# Необходимо заменить pass на Ваш код
def solution(node, idx):
    if idx == 0:
        newHead = node.next_item
        node.next_item = None
        return  newHead
    head = node
    for i in range(idx - 1):
        node = node.next_item
    newCh = node.next_item.next_item
    node.next_item.next_item = None
    node.next_item = newCh
    return head
def test():
    task5 = Node("Реализовать операцию вывода на печать текущие задания в обратном порядке", None)
    task4 = Node("Реализовать операцию удаления элемента из списка", task5)
    task3 = Node("Реализовать операцию добавления элемента в список", task4)
    task2 = Node("Реализовать функцию, которая выведет на печать в терминале список текущих заданий", task3)
    task1 = Node("Реализовать связанный список", task2)
    task0 = Node("Проверить занимаемый данными объем оперативной памяти", task1)
    new_head = solution(task0, 5)
    new_head = solution(new_head, 2)
    new_head = solution(new_head, 0)
    # result is Реализовать связанный список -> Реализовать операцию добавления элемента в список -> Реализовать операцию удаления элемента из списка -> None
    print_linked_list(new_head)

test()