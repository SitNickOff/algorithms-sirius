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
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

    def get(self):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

    def put(self, value):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

def worker(commands):
    #  Your code
    #  “ヽ(´▽｀)ノ”
    pass

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