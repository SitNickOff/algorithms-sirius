class Queue:
    def __init__(self, n) -> None:
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

    def push(self, x):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

    def pop(self):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass
        
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
