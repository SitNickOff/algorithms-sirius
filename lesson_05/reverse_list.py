class DoubleConnectedNode:  
    def init(self, value, next = None, prev = None):  
        self.value = value  
        self.next = next  
        self.prev = prev

def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")

def solution(node):
    while node.next != None:
        node = node.next
        # index -= 1
    while node:
        print(node.value, end=" -> ")
        node = node.prev
    print("None")

def test():
    task5 = DoubleConnectedNode("Реализовать операцию вывода на печать текущие задания в обратном порядке")
    task4 = DoubleConnectedNode("Реализовать операцию удаления элемента из списка")
    task3 = DoubleConnectedNode("Реализовать операцию добавления элемента в список")
    task2 = DoubleConnectedNode("Реализовать функцию, которая выведет на печать в терминале список текущих заданий")
    task1 = DoubleConnectedNode("Реализовать связанный список")
    task0 = DoubleConnectedNode("Проверить занимаемый данными объем оперативной памяти")

    task0.next = task1

    task1.next = task2
    task1.prev = task0

    task2.next = task3
    task2.prev = task1

    task3.next = task4
    task3.prev = task2
    
    task4.next = task5
    task4.prev = task3

    task5.prev = task4

    new_head = solution(task0)
    print_linked_list(new_head)

    # result: 
    # Реализовать операцию вывода на печать текущие задания в обратном порядке -> Реализовать 
    # операцию удаления элемента из списка -> Реализовать операцию добавления элемента в 
    # список -> Реализовать функцию, которая выведет на печать в терминале список текущих 
    # заданий -> Реализовать связанный список -> Проверить занимаемый данными объем 
    # оперативной памяти -> None

test()
