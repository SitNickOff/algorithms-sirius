class Queue:
    def __init__(self, n) -> None:
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = -1
        self.size = 0

    def is_empty(self):
        for el in self.queue:
            if el != None:
                return False
        return True

    def push(self, x):
        self.tail = (self.tail + 1) % self.max_n
        self.queue[self.tail] = x
        self.size += 1

    def pop(self):
        a = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return a
        
def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')

def full_test():
    q = Queue(8) 
    test(q.queue, [None, None, None, None, None, None, None, None])

    q.push(1)
    test(q.queue, [1, None, None, None, None, None, None, None])
    test(q.size, 1) 
    q.push(-1)
    q.push(0)
    q.push(11)
    test(q.queue, [1, -1, 0, 11, None, None, None, None])
    test(q.size, 4)

    q.pop()
    test(q.queue, [None, -1, 0, 11, None, None, None, None])
    test(q.size, 3)

    q.pop()
    q.pop()
    q.push(-8)
    q.push(7)
    q.push(3)
    q.push(16)
    test(q.queue, [None, None, None, 11, -8, 7, 3, 16])
    test(q.size, 5)
    q.push(12)
    test(q.queue, [12, None, None, 11, -8, 7, 3, 16])
    test(q.size, 6)

full_test()
