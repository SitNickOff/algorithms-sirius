# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def linear_search(numbers, x):
    for index in range(len(numbers)):   
        if numbers[index] == x:
            return index       
    return -1                   

list_num= list(map(int, input('Запишите числа, среди которых нужно искать: ').split())) 
num = int(input('Введите число, индекс которого нужно найти: ')) 
c = linear_search(list_num,num)

if c == -1:
    print('Всё работает, такого числа нет', c)
elif c != -1:
    print('Всё работает, такое число есть. Число', num ,'под индексом', c)
else:
    print('Ничего не работает, ошибка!!!')