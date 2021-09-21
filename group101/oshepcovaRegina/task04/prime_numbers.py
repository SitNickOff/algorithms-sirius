def isPrime(num):
    count = 0
    for j in range(2, num):
        if num % j == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False


def prime(num):
    result = list()
    for i in range(1, num+1):
        if isPrime(i):
            result.append(i)
    return result

print(prime(100))