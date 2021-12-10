import math, random

def insertion_sort(array):
    for i in range(len(array)):
        item_to_insert = array[i]
        j = i

        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1

        array[j] = item_to_insert
        # print(f'step {i}, sorted {i+1} elements: {array}')

insertion_sort([11, 2, 9, 7, 1])


digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6] # длины слов «ноль», «один»,...

def card_strength(card): # ключ сравнения
    return digit_lengths[card]

def insertion_sort_by_key(array, key):
    for i in range(0, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на сравнение ключей
        while j > 0 and key(item_to_insert) < key(array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert

cards = [3, 7, 9, 2, 3]
insertion_sort_by_key(cards, card_strength) 

# print(f'{cards}')


digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...

def is_first_card_weaker(card_1, card_2):  # функция-компаратор
    return digit_lengths[card_1] < digit_lengths[card_2]

# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(array, less):
  for i in range(1, len(array)):
    item_to_insert = array[i]
    j = i
    # заменим сравнение item_to_insert < array[j-1] на компаратор less
    while j > 0 and less(item_to_insert, array[j-1]):
      array[j] = array[j-1]
      j -= 1
    array[j] = item_to_insert

cards = [3, 7, 9, 2, 3]
insertion_sort_by_comparator(cards, is_first_card_weaker) 

# print(f'{cards}')


digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...

def key_for_card(card):
    return [-digit_lengths[card], card]

cards = [2, 3, 7]
cards.sort(key = key_for_card)

# print(f'{cards}')

cards2 = [2, 3, 7]
cards2 = sorted(cards2, key=lambda card: [-digit_lengths[card], card])
# print(f'{cards2}')

# print(math.nan)

def merge_sort(array):
    if len(array) == 1:  # базовый случай рекурсии
        return array
  
    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0 : len(array)/2])

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[len(array)/2 : len(array)])

    # заводим массив для результата сортировки
    result = [] * len(array)
    print(result)
  
    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
            k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left): 
        result[k] = left[l]   # перенеси оставшиеся элементы left в result
        l += 1
        k += 1  
    while r < len(right): 
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1
    
    return result 

# merge_sort([7, 3, 9, 0, 25])

def partition(array, pivot):
    less = [] # элементы array, меньшие pivot
    center = [pivot] # элементы array, равные pivot
    greater = [] # элементы array, большие pivot
    return less, center, greater

def quicksort(array):
    if len(array) < 2:  # базовый случай,
        return array       # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        random_index = random.randrange(len(array))
        pivot = array[random_index]
        less, center, greater = partition(array, pivot)

        return quicksort(less) + center + quicksort(greater) 

def counting_sort(array, k):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(k):
        for value in counted_values:
            array[index] = value
            index += 1 