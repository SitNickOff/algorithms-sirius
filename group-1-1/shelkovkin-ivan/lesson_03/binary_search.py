# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def sort(n): # чтобы искать число в списке, сначала надо его отсортировать для бинарного поиска
    for y in range(len(n)):
        for i in range(len(n)-y-1):
            if n[i] > n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]
    return n #возвращаем упорядочный массив

def binary_search(numbers, x):
    sor = sort(numbers)     #сортируем список
    lent = len(sor)-1     #будем идти от конца
    mid = len(sor) //2     # середина, которая ищит индекс
    zero = 0              #будем идти от начала
    print("отсортированный список: ", sor)
    while sor[mid] != x and zero <=lent:  # пока два условия выполняются цикл будет работать
        if x > sor[mid]:
            zero = mid +1
        else:
            lent = mid -1
        mid = (zero+lent)//2
    if zero > lent:
        return -1
    else:
        return mid

list_num = list(map(int, input("задайти список: ").split())) #задаем список чисел
x = int(input('введите число, индекс которого вы ищите')) #пользователь задает число, которое нам надо найти
poznany = binary_search(list_num, x)
if poznany == -1:
    print("Всё работает, такого числа нет,", poznany)
elif poznany != -1:
    print("Всё работает, такое число есть. Число", x ,"под индексом", poznany)
else:
    print("НИЧЕГО не работает. ---ОШИБКА---")