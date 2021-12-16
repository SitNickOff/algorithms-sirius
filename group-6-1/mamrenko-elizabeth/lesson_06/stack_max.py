# Реализуйте класс StackMax, поддерживающий операцию определения 
# максимума среди элементов в стеке. Сложность операции должна быть O(1). 
# Для пустого стека операция должна возвращать None. При этом push(x) и pop() 
# также должны выполняться за константное время.

# Формат ввода
# В первой строке записано одно число — количество команд, оно не превосходит 100000. 
# Далее идут команды по одной в строке. Команды могут быть следующих видов:
# push(x) — добавить число x в стек;
# pop() — удалить число с вершины стека;
# get_max() — напечатать максимальное число в стеке;
# Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».

# Формат вывода
# Для каждой команды get_max() напечатайте результат её выполнения. 
# Если стек пустой, для команды get_max() напечатайте «None». 
# Если происходит удаление из пустого стека — напечатайте «error».


class StackMaxEffective:
    def __init__(self):
        self.max = []
        self.head = None
        self.items = []
    def push(self, item):
        self.items.append(item)

        if len(self.max) == 0:
            self.max.append(item)
        elif self.max[-1] >= item:
            self.max.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "error"
        else:
            if len(self.max) != 0 and self.max[-1] == self.items[-1]:
                self.max.pop()
            self.items.pop()
    def get_max(self):
        if len(self.max) == 0:
            return None
        else:
            return self.max[-1]


def worker(commands):
    res = []
    t = StackMaxEffective()
    for el in commands:
        if el == "pop":
            k = t.pop()
            if k == "error":
                res.append(k)
        elif el == "get_max":
            res.append(t.get_max())
        else:
            t.push(int((el.split("push "))[1]))
    return res

# n = int(input())
# commands = []
# for i in range(n):
#     commands.append(input())

# for result in worker(commands):
#     print(result)

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