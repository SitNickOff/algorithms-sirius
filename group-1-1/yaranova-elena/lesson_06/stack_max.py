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
        self.stack = []
        self.stack_new = []
        self._max = -10000

    def push(self, item):
        self.stack.append(int(item))
        

    def pop(self):
        if len(self.stack) == 0:
            self.stack_new.append('error')
        else:
            rel = self.stack.pop()

    def get_max(self):
        if len(self.stack) == 0:
            self.stack_new.append(None)
        else:
            for i in range(len(self.stack)):
                if int(self.stack[i]) > int(self._max):
                    self._max = self.stack[i]
            self.stack_new.append(self._max)
    def __get__(self):
        return self.stack_new


def worker(commands):
    # Your code
    #  “ヽ(´▽｀)ノ”
    pass

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