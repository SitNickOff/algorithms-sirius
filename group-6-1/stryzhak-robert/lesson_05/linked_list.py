class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
def print_linked_list(vertex):
        while vertex:
                print(vertex.value, end=" -> ")
                vertex = vertex.next
        print("None") 

# def get_node_by_index(node, index):
#         while index:
#             node = node.next
#             index -= 1
#         return node

# def insert_node(head, index, value):
#         new_node = Node(value)

#         if index == 0:
#             new_node.next = head
#             return new_node

#         previous_node = get_node_by_index(head, index-1)
#         new_node.next = previous_node.next 
#         previous_node.next = new_node
#         return head


node3 = Node('Node3')
node2 = Node('Node2', node3)
node1 = Node('Node1', node2)
node0 = Node('Node0', node1)

print_linked_list(node0)
print_linked_list(node2) 

# head = insert_node(node0, 2, 'Серединка')
# print_linked_list(head)

# head = insert_node(head, 5, 'Хвост')
# print_linked_list(head)

# head = insert_node(head, 0, 'Голова')
# print_linked_list(head)