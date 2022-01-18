class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

    def pop(self):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

    def peak(self):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

    def size(self):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

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