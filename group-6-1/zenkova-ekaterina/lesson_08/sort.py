import math, random

def insertion_sort(array):
    for i in range(len(array)):
        item_to_insert = array[i]
        j = i

        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1

        array[j] = item_to_insert
        
        print(f'step {i}, sorted {i+1} elements: {array}')

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

print(f'{cards}')


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

print(f'{cards}')


digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...

def key_for_card(card):
    return [-digit_lengths[card], card]

cards = [2, 3, 7]
cards.sort(key = key_for_card)

print(f'{cards}')

cards2 = [2, 3, 7]
cards2 = sorted(cards2, key=lambda card: [- digit_lengths[card], card])

print(f'{cards2}')

        # print(math.nan)

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

print(merge_sort([7, 3, 9, 0, 25], 0, 5))




def partition(nums, low, high):  
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):  
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


# Проверяем, что оно работает
random_list_of_nums = [2, 1, 10, 7, 9, 5, 4, 6, 11]  
quick_sort(random_list_of_nums)  
print(random_list_of_nums) 

def counting_sort(array, k):
    counted_values = [0] * (k + 1)
    for value in range(len(array)):
        counted_values[array[value]] = counted_values[array[value]] + 1

    counted_values[0] = counted_values[0] - 1

    for value in range(1, k + 1):
        counted_values[value] = counted_values[value] + counted_values[value - 1]

    result = [None] * len(array)

    for i in reversed(array):
        result[counted_values[i]] = i
        counted_values[i] = counted_values[i] - 1

    return result

array = input('Введите массив: ').split()
array = [int(x) for x in array]
largest = max(array)
sorted_list = counting_sort(array, largest)
print('Отсортированный массив: ', end = '')
print(sorted_list)