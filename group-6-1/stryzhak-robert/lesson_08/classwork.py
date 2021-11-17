def insert_sort(array):
    for i in range(len(array)):
        # print(f'i: {i}, value: {array[i]}')

        item_to_insert = array[i]
        j = i

        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1

        array[j] = item_to_insert
        print(f'step {i}, sorted {i + 1} elements: {array}')


# insert_sort([9, 7, 4, 8, 2])

digit_length = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # ноль, один, два, три, четыре...


def key(index):
    return digit_length[index]


def insert_sort_by_key(array):
    for i in range(len(array)):
        # print(f'i: {i}, value: {array[i]}')

        item_to_insert = array[i]
        j = i

        while j > 0 and key(item_to_insert) < key(array[j - 1]):
            array[j] = array[j - 1]
            j -= 1

        array[j] = item_to_insert
        print(f'step {i}, sorted {i + 1} elements: {array}')


# insert_sort_by_key([9, 7, 2, 4, 8, 3])

def less(a, b):
    if [digit_length[a], a] < [digit_length[b], b]: return True

    return False


def insert_sort_by_comporator(array, comporator):
    for i in range(len(array)):
        # print(f'i: {i}, value: {array[i]}')

        item_to_insert = array[i]
        j = i

        while j > 0 and comporator(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1

        array[j] = item_to_insert
        print(f'step {i}, sorted {i + 1} elements: {array}')


# insert_sort_by_comporator([9, 7, 2, 4, 8, 3], less)

# [5, 7, 1, 0, 1, 5, 11, 1]
# [1, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0]

def merge_sort(array):
    if len(array) == 1:
        return array
    left = merge_sort(array[0: len(array) / 2])
    result =
