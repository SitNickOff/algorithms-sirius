class StackMaxEffective:
    def init(self):
        self.items = []
        self.maxx = []

    def push(self, item):
        self.items.append(item)
        
        if len(self.maxx) == 0:
            self.maxx.append(item)
        else:
            if item > self.maxx[len(self.maxx)-1]:
                self.maxx.append(item)
            else:
                self.maxx.append(self.maxx[len(self.maxx)-1])
        

    def pop(self):
        if len(self.items) == 0:
            return "error"
        else:
            self.maxx.pop()
            return self.items.pop()


    def get_max(self):
        if len(self.maxx) == 0:
            return None
        else:
            return self.maxx[len(self.maxx)-1]
        

def worker(commands):
    res = []
    stack = StackMaxEffective()
    for command in commands:
        if command == 'pop':
            if stack.pop() == 'error':
                res.append('error')
        elif command == 'get_max':
            res.append(stack.get_max())
        else:
            stack.push(int(command.split()[1]))
    return res


def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')

test(
    worker(['pop', 'pop', 'push 4', 'push -5', 'push 7', 'pop', 'pop', 'get_max', 'pop', 'get_max']),
    ['error', 'error', 4, None]
)
test(
    worker(['get_max', 'push -6', 'pop', 'pop', 'get_max', 'push 2', 'get_max', 'pop', 'push -2', 'push -6']),
    [None, 'error', None, 2]
)
