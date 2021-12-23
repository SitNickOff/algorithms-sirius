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
        self.items = []

    def push(self, item):
        if self.items:
            max_ = max(item, self.items[-1][1])
        else:
            max_ = item
        self.items.append((item, max_))

    def pop(self):
        return self.items.pop()[0]

    def get_max(self):
        return self.items[-1][1]


stack = StackMaxEffective()


def worker(commands):
    for command in commands:
        tmp = command.split()
        if tmp[0] == 'pop':
            if len(stack.items) > 0:
                stack.pop()
            else:
                print('error')
        elif tmp[0] == 'push':
            stack.push(int(tmp[1]))
        elif tmp[0] == 'get_max':
            if len(stack.items) > 0:
                print(stack.get_max())
            else:
                print('None')
        else:
            print('Command not found!')
            continue


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