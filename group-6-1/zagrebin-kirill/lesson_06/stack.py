class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')

stack = Stack()
test(stack.size(), 0)  
test(stack.items, []) 
stack.push(7)
test(stack.size(), 1) 
test(stack.items, [7]) 
print(f'stack.size: {stack.size()} - {stack.items}')
stack.push(11)
test(stack.size(), 2) 
test(stack.items, [7, 11])    
print(f'stack.size: {stack.size()} - {stack.items}')
test(stack.pop(), 11) 
test(stack.size(), 1) 
test(stack.items, [7])
print(f'stack.size: {stack.size()} - {stack.items}')
test(stack.peak(), 7) 
test(stack.size(), 1) 
test(stack.items, [7])
print(f'stack.size: {stack.size()} - {stack.items}')