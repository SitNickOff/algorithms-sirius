# Оперативная память (ОЗУ)

import sys

print(sys.getsizeof(3), 3)  # => 28 байт занимает короткое целое число
print(sys.getsizeof(42), 42)  # => 28 байт занимает короткое целое число
print(sys.getsizeof(214748364), 2147483646)  # => 28 байт занимает короткое целое число
print(sys.getsizeof(2147483647), 2147483647)  # => 28 байт занимает короткое целое число
print(sys.getsizeof(''), 'пустая строка')  # => 49 байт занимает буква
print(sys.getsizeof(' '), 'пробел')  # => 50 байт занимает пробел
print(sys.getsizeof('a'), 'a')  # => 50 байт занимает буква
print(sys.getsizeof('ab'), 'ab')  # => 51 байт занимает буква
print(sys.getsizeof('abcdex'), 'abcdex')  # => 55 байт занимает короткое слово
print(sys.getsizeof([]), [])  # => 56 байт занимает пустой массив
print(sys.getsizeof([42]), 1) # => 64 = (56 + 8) байт занимает массив с одним элементом.
print(sys.getsizeof([1, 2]), 2) # 72 = (56 + 8 * 2)
print(sys.getsizeof([1, 2, 3]), 3) # 120 = (56 + 8 * 2)
print(sys.getsizeof([1, 2, 3, 4]), 4) # 120 = (56 + 8 * 2)
print(sys.getsizeof([1, 2, 3, 4, 5]), 5) # 120 = (56 + 8 * 2)
print(sys.getsizeof([1, 2, 3, 4, 5, 6]), 6) # 152 = (56 + 8 * 12)
print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7]), 7) # 120 = (56 + 8 * 2)
print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8]), 8) # 120 = (56 + 8 * 2)
print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9) # 152 = (56 + 8 * 2)
print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10) # 152 = (56 + 8 * 2)