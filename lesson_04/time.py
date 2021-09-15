import time

time_start = time.time()

x = 100000000
while x > 0:
    x-=1

time_finish = time.time()
time_span =  time_finish - time_start
print(time_span)