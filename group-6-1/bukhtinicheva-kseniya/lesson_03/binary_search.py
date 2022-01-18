# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def binary_search(numbers, x):
  low=0
  high=len(numbers) - 1

  while low<=high:
    middle = (low+high) //2

    if numbers[middle]==x:
        return middle

    elif numbers[middle]>x:
        high = middle - 1

    elif numbers[middle]<x:
        low = middle + 1
        
  return -1

numbers=[2,3,4,5,6,7]
print(numbers)
print(binary_search(numbers,2))
    



    
