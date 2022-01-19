# Сортировка слиянием

# Ограничение времени	2 секунды
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt

# Гоше дали задание написать красивую сортировку слиянием. Поэтому Гоше 
# обязательно надо реализовать отдельно функцию merge и функцию merge_sort.
# 
# Функция merge принимает два отсортированных массива, сливает их в один 
# отсортированный массив и возвращает его. Если требуемая сигнатура имеет 
# вид merge(array, left, mid, right), то первый массив задаётся полуинтервалом 
# [left, mid) массива array, а второй – полуинтервалом [mid, right) массива array.
# 
# Функция merge_sort принимает некоторый подмассив, который нужно отсортировать. 
# Подмассив задаётся полуинтервалом — его началом и концом. Функция должна 
# отсортировать передаваемый в неё подмассив, она ничего не возвращает.
# 
# Функция merge_sort разбивает полуинтервал на две половинки и рекурсивно вызывает 
# сортировку отдельно для каждой. Затем два отсортированных массива сливаются 
# в один с помощью merge.
# 
# Заметьте, что в функции передаются именно полуинтервалы [begin, end), то есть 
# правый конец не включается. Например, если вызвать merge_sort(arr, 0, 4), где 
# arr = [4, 5, 3, 0, 1, 2], то будут отсортированы только первые четыре элемента, 
# изменённый массив будет выглядеть как arr = [0, 3, 4, 5, 1, 2].
# 
# Реализуйте эти две функции.

def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]
    k = lf
    i = 0
    j = 0

    while (lf + i < mid and mid + j < rg):
        if (left[i] <= right[j]):
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    if lf + i < mid:
        while k < rg:
            arr[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < rg:
            arr[k] = right[j]
            j = j + 1
            k = k + 1
    
    return arr

def merge_sort(arr, lf, rg):

    if rg - lf > 1:
        mid = (lf + rg)//2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)

    return arr
 
def test(arr, lf, mid, rg, result):
    if merge(arr, lf, mid, rg) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', merge(arr, lf, mid, rg))
    else:
        print('Отлично: ', result, '==', merge(arr, lf, mid, rg))
        
test([1, 4, 9, 2, 10, 11], 0, 3, 6, [1, 2, 4, 9, 10, 11])

def test1(arr, lf, rg, result):
    if merge_sort(arr, lf, rg) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', merge_sort(arr, lf, rg))
    else:
        print('Отлично: ', result, '==', merge_sort(arr, lf, rg))

test1([1, 4, 2, 10, 1, 2], 0, 6, [1, 1, 2, 2, 4, 10])