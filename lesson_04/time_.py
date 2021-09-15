import time

time_start = time.time()

i = 0

while i < 1000000:
    i += 1

time_middle = time.time()

i = 0

while i < 1000000:
    i += 1

time_finish = time.time()

time_span1 = time_middle - time_start
time_span2 = time_finish - time_middle
time_span = time_finish - time_start

print('part 1: ', time_span1)
print('part 2: ', time_span2)
print('total: ', time_span)