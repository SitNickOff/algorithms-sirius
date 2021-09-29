import time


def is_prime(num):
    if num <= 1:
        return False
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1
    return True


start = time.time()
print(is_prime(104683))
print(time.time() - start)
