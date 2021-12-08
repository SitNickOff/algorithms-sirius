# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и
# вернуть его индекс. Если x в массиве не встречается - вернуть -1.

# Решить задачу применяя алгоритм бинарного поиска

def binary_search(mass, item):
  low = 0
  high = len(mass) - 1
  i = 0
  while low <= high:
    mid = (low + high) // 2
    guess = mass[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
    i += 1
  return -1

m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(m, 3))
print(binary_search(m, 86))