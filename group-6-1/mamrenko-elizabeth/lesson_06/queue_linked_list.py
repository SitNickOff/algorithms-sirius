# Списочная очередь

# Очередь должна поддерживать выполнение трёх команд:

# get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста, то вывести «error».
# put(x) — добавить число x в очередь
# size() — вывести текущий размер очереди

# Формат ввода
# В первой строке записано количество команд n — целое число, не превосходящее 1000. 
# В каждой из следующих n строк записаны команды по одной строке.

# Формат вывода
# Выведите ответ на каждый запрос по одному в строке.

class Node:  
    def __init__(self, value, next_item = None):  
        self.value = value  
        self.next_item = next_item

class Queue:  
    def __init__(self):  
        self.size = 0
        self.header = None
        self.tail = None

    def size(self):
        return self.size

    def get(self):
        if self.header:
            self.size -= 1
            a = self.header.value
            print(a)
            self.header = self.header.next_item
            return a

    def put(self, value):
        self.size += 1
        if not self.header:
            self.header = Node(value)
        elif self.size == 1:
            self.tail = Node(value, self.header)
            self.header = Node(self.header.value, self.tail)
        else:
            self.tail = Node(value, self.tail)


def worker(commands):
    t = Queue()
    res = []
    for el in commands:
        if el == "get":
            k = t.get()
            if k == None:
                res.append("error")
            else:
                res.append(k)
        elif el == "size":
            res.append(t.size)
        else:
            t.put(int((el.split("put "))[1]))

    return res

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