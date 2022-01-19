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
        self.maximum = [] 
        self.size = 0        

    def push(self, item):               
        self.items.append(item)        
        if len(self.maximum) == 0:
            self.maximum.append(item)
        elif item > self.maximum[self.size - 1]:
            self.maximum.append( item )
        else:
            self.maximum.append( self.maximum[self.size - 1] )
        self.size += 1 
        print(f'size: {self.size} - {self.items} - {self.maximum}')
           

    def pop(self):
        
        if len(self.items) == 0:
            return 'error'
        else:
            self.size -= 1
            self.maximum.pop()
            return self.items.pop()
        

    def get_max(self):
        
        if len(self.items) == 0:
            return None
        else:
            return self.maximum[self.size-1]
    
def worker(commands):
    result = []
    stack = StackMaxEffective()
    
    for command in commands:
        if command == 'pop':
            if stack.pop() == 'error':
                result.append('error')                
        elif command == 'get_max':
            result.append(stack.get_max())
        else:
            stack.push(int(command.split(' ')[1]))
    
    return result
    
    
    
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