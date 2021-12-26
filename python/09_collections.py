import sys
import timeit

# Сравниваем коллекции

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
dict = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11,
    12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20
}
set = set(list)

print('list_size', sys.getsizeof(list))
print('tuple_size', sys.getsizeof(tuple))
print('dict_size', sys.getsizeof(dict))
print('set_size', sys.getsizeof(set))


print('')
print('---' * 10)
print('')

list_test = '''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

list_time = timeit.timeit(list_test, number=1000000)
print('list_time', list_time)

tuple_test = '''
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
'''

tuple_time = timeit.timeit(tuple_test, number=1000000)
print('tuple_time', tuple_time)

dict_test = '''
dict = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11,
    12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20
}
'''

dict_time = timeit.timeit(dict_test, number=1000000)
print('dict_time', dict_time)

set_test = '''
set1 = set([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
])
'''

set_time = timeit.timeit(set_test, number=1000000)
print('set_time', set_time)
