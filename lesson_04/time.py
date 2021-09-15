import time

time_start = time.time()

i = 0
while i < 1000:
    i += 1

time_middle = time.time()

i = 0
while i < 1000000:
    i += 1


time_finish = time.time()

time_span = time_finish - time_start
time_span1 = time_middle - time_start
time_span2 = time_finish - time_middle

print(time_span)
print('part 1', time_span1)
print('part2', time_span2)