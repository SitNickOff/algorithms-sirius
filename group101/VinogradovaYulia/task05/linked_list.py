class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
def print_linked_list(vertex):
        while vertex:
                print(vertex.value, end=" -> ")
                vertex = vertex.next
        print("None")


node3 = Node('Node3')
node2 = Node('Node2', node3)
node1 = Node('Node1', node2)
node0 = Node('Node0', node1)

print_linked_list(node0)
print_linked_list(node2) 