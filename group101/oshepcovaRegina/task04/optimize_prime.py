def isPrime(num):
    div = 2

    while div * div <= num:
      if num % div == 0:
        return False
      div += 1
    return True

def optimize_prime(num):
    result = list()
    for i in range(1, num+1):
        if isPrime(i):
            result.append(i)
    return result

print(optimize_prime(100))
