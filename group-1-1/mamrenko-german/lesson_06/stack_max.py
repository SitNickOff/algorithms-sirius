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
        self.maks = []

    def push(self, item):
        self.items.append(item)
        if len(self.maks) == 0:
            self.maks.append(item)
        else:
            if item > self.maks[len(self.maks)-1]:
                self.maks.append(item)
            else:
                self.maks.append(self.maks[len(self.maks)-1])
        

    def pop(self):
        if len(self.items) == 0:
            return "error"
        else:
            self.maks.pop()
            return self.items.pop()

    def get_max(self):
        if len(self.maks) == 0:
            return None
        else:
            return self.maks[len(self.maks)-1]


def worker(coms):
    list_ = []
    stack = StackMaxEffective()
    for com in coms:
        if com == "pop":
            if stack.pop() == "error":
                list_.append("error")
        elif com == "get_max":
            list_.append(stack.get_max())
        else:
            stack.push(int(com.split()[1]))
    return list_

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