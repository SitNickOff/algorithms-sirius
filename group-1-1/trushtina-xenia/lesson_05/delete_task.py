# Напишите функцию solution, 
# которая принимает на вход голову списка и номер удаляемого дела и 
# возвращает голову обновлённого списка.

# Внимание: в этой задаче не нужно считывать входные данные. Нужно написать 
# только функцию, которая принимает на вход голову списка и номер удаляемого 
# элемента и возвращает голову обновлённого списка.

class Node:  
    def __init__(self, value, next_item=None):  
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

def solution(node, self):
    node.val = node.next.val
    node.next = node.next.next