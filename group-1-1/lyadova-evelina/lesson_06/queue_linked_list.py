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
class Stack:
    def __init__(self):
        self.stack = []
        self.stack_new=[]

    def get(self):
        if len(self.stack) == 0:
            self.stack_new.append('error')
        else: 
            removed = int(self.stack.pop(0))
            self.stack_new.append(removed)

    def put(self, item):
        self.stack.append(item)
    
    def size(self):
        self.stack_new.append(len(self.stack))

    def _get_(self):
        return self.stack_new

   
def workw(commands):
    
    commandes = Stack()
    for i in range(len(commands)):
        if ' ' in commands[i]:
            command, number = commands[i].split()
        else: command = commands[i]
        if command == 'put':
            commandes.put(number)
        if command == 'get':
            commandes.get()
        if command == 'size':
            commandes.size()
    return commandes._get_()

def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')

test(
    workw(['put -34', 'put -23', 'get', 'size', 'get', 'size', 'get', 'get', 'put 80', 'size']),
    [-34, 1, -23, 0, 'error', 'error', 1]
)
test(
    workw(['put -66', 'put 98', 'size', 'size', 'get', 'get']),
    [2, 2, -66, 98]
)
test(
    workw(['get', 'size', 'put 74', 'get', 'size', 'put 90', 'size', 'size', 'size']),
    ['error', 0, 74, 0, 1, 1, 1]
)