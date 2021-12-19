class DoubleConnectedNode:  
    def __init__(self, value, next = None, prev = None):  
        self.value = value  
        self.next = next  
        self.prev = prev

def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")

def solution(self, head):
    prev = None
    cur = head

    while cur:
        n = cur.next
        cur.next = prev
        prev = cur
        cur = n
    
    return prev