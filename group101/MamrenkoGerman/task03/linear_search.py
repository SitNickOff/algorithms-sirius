def find_element(numbers, x):

    for index in (len(numbers)):  # проходим по всем элементам массива

        if numbers[index] == x:  # сравниваем их с иксом

            return index  # если нашли - возвращаем индекс

    return -1  # если не нашли - возвращаем -1