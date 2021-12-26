class Stack:
    def __init__(self):
        self.stack = []

    def get(self):
        if len(self.stack) == 0:
            return 'error'
        else: 
            removed = int(self.stack.pop(0))
            return removed

    def put(self, item):
        self.stack.append(item)
    
    def size(self):
        return len(self.stack)


   
def worker(commands):
    commandes = Stack()
    result = []
    for i in range(len(commands)):
        if ' ' in commands[i]:
            command, number = commands[i].split()
        else: command = commands[i]
        if command == 'put':
            commandes.put(number)
        if command == 'get':
            result.append(commandes.get())
        if command == 'size':
            result.append(commandes.size())
    return result
    
# count_commands = int(input())
# commands = []
# for i in range(count_commands):
#     commands.append(input())

# for result in worker(commands):
#     print(result)

def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')

test(
    worker(['put -34', 'put -23', 'get', 'size', 'get', 'size', 'get', 'get', 'put 80', 'size']),
    [-34, 1, -23, 0, 'error', 'error', 1]
)
test(
    worker(['put -66', 'put 98', 'size', 'size', 'get', 'get']),
    [2, 2, -66, 98]
)
test(
    worker(['get', 'size', 'put 74', 'get', 'size', 'put 90', 'size', 'size', 'size']),
    ['error', 0, 74, 0, 1, 1, 1]
)