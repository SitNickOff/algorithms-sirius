# Нужно распечатать список задач занятия №5.
# Напишите функцию, которая печатает задачи занятия №5

# Внимание: в этой задаче не нужно считывать входные данные. 
# Нужно написать только функцию, которая принимает на вход голову списка и печатает его элементы. 

class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

# Необходимо заменить pass на Ваш код
def solution(node):
     while node:
        print(node.value)
        node = node.next_item
 

def test():
    task5 = Node("Реализовать операцию вывода на печать текущие задания в обратном порядке", None)
    task4 = Node("Реализовать операцию удаления элемента из списка", task5)
    task3 = Node("Реализовать операцию добавления элемента в список", task4)
    task2 = Node("Реализовать функцию, которая выведет на печать в терминале список текущих заданий", task3)
    task1 = Node("Реализовать связанный список", task2)
    task0 = Node("Проверить занимаемый данными объем оперативной памяти", task1)
    solution(task0)
    # Output is:
    # Проверить занимаемый данными объем оперативной памяти
    # Реализовать связанный список
    # Реализовать функцию, которая выведет на печать в терминале список текущих заданий
    # Реализовать операцию добавления элемента в список
    # Реализовать операцию удаления элемента из списка
    # Реализовать операцию вывода на печать текущие задания в обратном порядке

test()